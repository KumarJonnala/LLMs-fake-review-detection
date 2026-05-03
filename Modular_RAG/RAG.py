"""
Multi-Dataset × Multi-Model RAG Evaluation for Fake Review Detection
---------------------------------------------------------------------
Outer loop : CSV datasets
Inner loop  : Ollama LLM models
Output      : results.json  (dataset path → model → metrics + confusion matrix)
"""

import os
import json
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────

os.environ["OLLAMA_HOST"] = "http://localhost:8500"
# Each entry: (csv_path, label_column_name)
DATASETS = [
    ("/home/anuj97og/fake_reviews_prediction/Datasets/Amazon_Human_VS_ComputerFake.csv",       "Binary_label"),
    ("/home/anuj97og/fake_reviews_prediction/Datasets/Hotel_Human_VS_HumanFake_relabelled.csv", "Binary_label"),
    ("/home/anuj97og/fake_reviews_prediction/Datasets/Hotel_HumanReal_VS_CG.csv",               "Binary_label"),
    ("/home/anuj97og/fake_reviews_prediction/Datasets/Hotel_HumanReal_VS_MixFake.csv",          "Binary_label"),
]

MODELS_TO_EVALUATE = [
    "gemma3:12b",
    "gemma3:27b",
    "llama3:8b",  
    "phi4:14b",
]

RETRIEVER_K      = 5
VECTORSTORE_PATH = "temp_vectorstore"
OUTPUT_JSON      = "resultsV5_2_Amazon.json"

# ─────────────────────────────────────────────
# SHARED EMBEDDINGS (loaded once)
# ─────────────────────────────────────────────

print("Loading embedding model...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ─────────────────────────────────────────────
# PROMPT
# ─────────────────────────────────────────────

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

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def build_vectorstore(df_train: pd.DataFrame) -> FAISS:
    """Build a fresh FAISS vectorstore from the training split."""
    documents = [
        Document(page_content=row["text"], metadata={"label": row["label"]})
        for _, row in df_train.iterrows()
    ]
    vs = FAISS.from_documents(documents, embeddings)
    vs.save_local(VECTORSTORE_PATH)
    return FAISS.load_local(VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True)


def format_examples(docs) -> str:
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


def classify_review(review_text: str, llm, retriever) -> str:
    docs     = retriever.invoke(review_text)
    examples = format_examples(docs)
    prompt   = rag_prompt.format(examples=examples, review=review_text)
    response = llm.invoke(prompt)
    return normalize_prediction(response)


def cm_to_serializable(cm: np.ndarray) -> dict:
    """Convert a 2×2 confusion matrix to a JSON-friendly dict."""
    return {
        "true_fake_pred_fake": int(cm[0][0]),
        "true_fake_pred_real": int(cm[0][1]),
        "true_real_pred_fake": int(cm[1][0]),
        "true_real_pred_real": int(cm[1][1]),
    }


# ─────────────────────────────────────────────
# MAIN EVALUATION LOOPS
# ─────────────────────────────────────────────

final_output = {
    "run_timestamp": datetime.now().isoformat(),
    "models_evaluated": MODELS_TO_EVALUATE,
    "datasets": {}
}

for csv_path, label_col in DATASETS:
    dataset_key = os.path.basename(csv_path)
    print(f"\n{'#'*65}")
    print(f"  DATASET: {dataset_key}")
    print(f"{'#'*65}")

    # ── Load & split ──────────────────────────
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"  [SKIP] File not found: {csv_path}")
        final_output["datasets"][csv_path] = {"error": "File not found"}
        continue

    df.rename(columns={label_col: "label"}, inplace=True)

    if "text" not in df.columns or "label" not in df.columns:
        print(f"  [SKIP] Missing required columns in {dataset_key}")
        final_output["datasets"][csv_path] = {"error": "Missing 'text' or 'label' column"}
        continue

    df_train, df_test = train_test_split(
        df, test_size=0.5, random_state=42, stratify=df["label"]
    )
    print(f"  Total: {len(df)} | Train: {len(df_train)} | Test: {len(df_test)}")

    # ── Build vectorstore (once per dataset) ──
    print("  Building vector store...")
    vectorstore = build_vectorstore(df_train)
    retriever   = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": RETRIEVER_K}
    )

    dataset_results = {
        "csv_path":    csv_path,
        "total_rows":  len(df),
        "train_rows":  len(df_train),
        "test_rows":   len(df_test),
        "models":      {}
    }

    for model_name in MODELS_TO_EVALUATE:
        print(f"\n  {'='*55}")
        print(f"    Model: {model_name}")
        print(f"  {'='*55}")

        llm = OllamaLLM(model=model_name)

        y_true, y_pred = [], []
        unknown_count  = 0

        for idx, row in df_test.iterrows():
            review     = row["text"]
            true_label = row["label"]
            pred_label = classify_review(review, llm, retriever)

            y_true.append(true_label)
            y_pred.append(pred_label)

            if pred_label == "UNKNOWN":
                unknown_count += 1

            print(f"    [{idx}] True: {true_label} | Pred: {pred_label}")

        # ── Filter UNKNOWNs before metrics ────
        filtered = [(t, p) for t, p in zip(y_true, y_pred) if p != "UNKNOWN"]
        if filtered:
            y_true_f, y_pred_f = zip(*filtered)
        else:
            y_true_f, y_pred_f = [], []

        accuracy = accuracy_score(y_true_f, y_pred_f) if y_true_f else 0.0
        f1       = f1_score(y_true_f, y_pred_f, pos_label="fake", zero_division=0) if y_true_f else 0.0
        cm       = confusion_matrix(y_true_f, y_pred_f, labels=["fake", "real"]) if y_true_f else np.zeros((2, 2), dtype=int)

        print(f"\n    Accuracy      : {accuracy:.4f}")
        print(f"    F1 (fake)     : {f1:.4f}")
        print(f"    Confusion Matrix [fake | real]:\n    {cm}")

        dataset_results["models"][model_name] = {
            "accuracy": round(accuracy, 4),
            "f1_fake":  round(f1, 4),
            "confusion_matrix": {
                "labels": ["fake", "real"],
                "matrix": cm_to_serializable(cm),
            },
        }

    final_output["datasets"][csv_path] = dataset_results

# ─────────────────────────────────────────────
# SAVE JSON
# ─────────────────────────────────────────────

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=2, ensure_ascii=False)

print(f"\n\n{'='*65}")
print(f"  Results saved to: {OUTPUT_JSON}")
print(f"{'='*65}")

# ─────────────────────────────────────────────
# PRINT FINAL SUMMARY TABLE
# ─────────────────────────────────────────────

print(f"\n{'='*65}")
print("  FINAL SUMMARY")
print(f"{'='*65}")

for csv_path, ds_data in final_output["datasets"].items():
    if "error" in ds_data:
        print(f"\n  {os.path.basename(csv_path)}: ERROR — {ds_data['error']}")
        continue

    print(f"\n  {os.path.basename(csv_path)}")
    print(f"  {'Model':<20} {'Accuracy':>10} {'F1 (fake)':>12} {'Unknown':>9}")
    print(f"  {'-'*53}")
    for model_name, metrics in ds_data["models"].items():
        print(
            f"  {model_name:<20} "
            f"{metrics['accuracy']:>10.4f} "
            f"{metrics['f1_fake']:>12.4f} "
            f"{metrics['unknown_predictions']:>9}"
        )

print("\nDone.")