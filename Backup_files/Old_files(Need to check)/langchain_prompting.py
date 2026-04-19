import pandas as pd
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from config_prompt import Config
from evaluate import evaluate_model


print(Config.file_path)

# Load your CSV
df = pd.read_csv(Config.file_path, engine="python")
reviews = df["text"].tolist()

print("Loaded rows:", len(df))
print(df.head(2))

# Ollama llm
llm = OllamaLLM(
    model="llama3.2:3b",          
    base_url="http://127.0.0.1:11434",
    temperature=0.0 
)

# Define zero-shot classification prompt
prompt = PromptTemplate(
    input_variables=["text"], # the placeholder to be replaced based on prompt template
    template=Config.zero_shot_prompt_template1
)

chain = prompt | llm

# Classify each review
results = []

for i, r in enumerate(reviews):
    print(f"[{i+1}/{len(reviews)}] running inference", flush=True)

    result = chain.invoke({"text": r})
    label = result.strip().lower().split()[0].strip(".,!?;:")

    print(label)
    results.append(label)

print("Number of samples:", len(df))
print("Number of predictions:", len(results))
print("Unique predictions:", set(results))

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