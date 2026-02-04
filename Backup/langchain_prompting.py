import pandas as pd
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain import LLMChain
from config import Config
from evaluate import evaluate_model

# Load your CSV
df = pd.read_csv(Config.file_path)[350:450].reset_index(drop=True)
reviews = df["text"].tolist()

# Ollama llm
llm = OllamaLLM(
    model="llama3.2:3b",          
    base_url="http://127.0.0.1:11434",
    temperature=0.0 
)

# Define zero-shot classification prompt
prompt = PromptTemplate(
    input_variables=["text"], # the placeholder to be replaced based on prompt template
    template=Config.zero_shot_prompt_template
)

# Classify each review
results = []
for r in reviews:
    result = chain.invoke({"text": r})
    # Clean the output - extract only "truthful" or "deceptive"
    label = result.strip().lower()
    # Extract first word if model adds extra text
    if " " in label:
        label = label.split()[0]
    # Remove any punctuation
    label = label.strip('.,!?;:')
    print(f"Raw output: {result} -> Cleaned: {label}")
    results.append(label)

accuracy, f1, conf_matrix = evaluate_model(df, results)

print("=" * 50)
print("ZERO-SHOT PROMPTING RESULTS")
print("=" * 50)
print("Accuracy:", accuracy)
print("\nF1 Score:", f1)
print("\nConfusion Matrix:")
print(conf_matrix)
print("=" * 50)

# Add results back to DataFrame
df["prediction"] = results

# Save outputs
df.to_csv("classified_reviews.csv", index=False)

print(df.head())