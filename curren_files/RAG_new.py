# Generated from: RAG_new.ipynb
# Converted at: 2026-04-19T11:12:31.088Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report

from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

os.environ["OLLAMA_HOST"] = "http://localhost:8000"

CSV_PATH = r"/home/anuj97og/fake_reviews_prediction/Datasets/Amazon_Human_VS_ComputerFake.csv"
VECTORSTORE_PATH = "hotel_review_vectorstore"
RETRIEVER_K = 5

MODELS_TO_EVALUATE = [
    "gemma3:12b",
    "gemma3:27b",
    "llama3:8b"
    #"phi3:7b",
    #"phi3:14b",
]

df = pd.read_csv(CSV_PATH)
df.rename(columns={"Binary_label": "label"}, inplace=True)

df_set1, df_set2 = train_test_split(
    df, test_size=0.5, random_state=42, stratify=df["label"]
)
print(f"Total: {len(df)} | Train (vector store): {len(df_set1)} | Test: {len(df_set2)}")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    Document(page_content=row["text"], metadata={"label": row["label"]})
    for _, row in df_set1.iterrows()
]

vectorstore = FAISS.from_documents(documents, embeddings)
vectorstore.save_local(VECTORSTORE_PATH)

vectorstore = FAISS.load_local(
    VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

rag_prompt = PromptTemplate(
    input_variables=["examples", "review"],
    template="""
    You are an expert at detecting fake and real reviews of Amazon products. Carefully analyze the following review for signs such as:

    Task: Classify the following review of a  Amazon product as either "real" or "fake". Carefully analyze the following review for signs such as:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Repetitive or templated phrasing
    - Marketing-like wording or unnatural flow
    - Specific details vs. general statements

    Here are some examples:
    {examples}

    Now classify this review:
    "{review}"

    Classify this review as either "real" or "fake" (respond with only one word):
    """
)

def format_examples(docs):
    return "\n\n".join(
        f'Review: "{d.page_content}"\nLabel: {d.metadata["label"]}'
        for d in docs
    )


def normalize_prediction(response: str) -> str:
    r = response.strip().lower()
    if "fake" in r:
        return "fake"
    if "real" in r:
        return "real"
    return "UNKNOWN"


def classify_review(review_text: str, llm) -> str:
    docs = retriever.invoke(review_text)
    examples = format_examples(docs)
    prompt = rag_prompt.format(examples=examples, review=review_text)
    response = llm.invoke(prompt)
    return normalize_prediction(response)

all_results = []   # list of dicts for final summary table

for model_name in MODELS_TO_EVALUATE:
    print(f"\n{'='*60}")
    print(f"  Evaluating model: {model_name}")
    print(f"{'='*60}")

    llm = OllamaLLM(model=model_name)

    y_true, y_pred = [], []
    unknown_count = 0

    for idx, row in df_set2.iterrows():
        review = row["text"]
        true_label = row["label"]
        pred_label = classify_review(review, llm)

        y_true.append(true_label)
        y_pred.append(pred_label)

        if pred_label == "UNKNOWN":
            unknown_count += 1

        print(f"  [{idx}] True: {true_label} | Pred: {pred_label}")

    # ── Metrics ──────────────────────────────
    # Exclude UNKNOWN from metric calculation
    filtered = [(t, p) for t, p in zip(y_true, y_pred) if p != "UNKNOWN"]
    if filtered:
        y_true_f, y_pred_f = zip(*filtered)
    else:
        y_true_f, y_pred_f = [], []

    accuracy = accuracy_score(y_true_f, y_pred_f) if y_true_f else 0.0
    f1       = f1_score(y_true_f, y_pred_f, pos_label="fake", zero_division=0) if y_true_f else 0.0

    cm_fake_real = confusion_matrix(y_true_f, y_pred_f, labels=["fake", "real"]) if y_true_f else np.zeros((2, 2), dtype=int)

    print(f"  UNKNOWN preds : {unknown_count}")
    print(f"\n  Model         : {model_name}")
    print(f"  Accuracy      : {accuracy:.4f}")
    print(f"  F1 (fake)     : {f1:.4f}")
    print(f"  Confusion Matrix (rows=true, cols=pred) [fake | real]:")
    print(f"  {cm_fake_real}")
    if y_true_f:
        print(f"\n  Classification Report:")
        print(classification_report(y_true_f, y_pred_f, target_names=["fake", "real"], zero_division=0))

    all_results.append({
        "model":    model_name,
        "accuracy": accuracy,
        "f1_fake":  f1,
        "unknown":  unknown_count,
        "cm":       cm_fake_real,
        "y_true":   list(y_true_f),
        "y_pred":   list(y_pred_f),
    })
