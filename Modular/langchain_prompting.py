import importlib.util
import json
import os
from pathlib import Path

import pandas as pd
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

from config_model import ConfigModel

PROMPT_KEY = "ver_1"

def evaluate_model(df, predictions, label_col="Binary_label"):
    # Get true labels from the dataframe
    y_true = df[label_col].tolist()
    y_pred = predictions

    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average="weighted", pos_label=None)
    conf_matrix = confusion_matrix(y_true, y_pred)

    return accuracy, f1, conf_matrix


def run_prompt_eval(dataset_path, prompt_template, model, text_col="text"):
    
    df_local = pd.read_csv(dataset_path)
    reviews = df_local[text_col].tolist()

    prompt = PromptTemplate(
        input_variables=["text"],
        template=prompt_template,
    )

    ollama_host = os.environ.get("OLLAMA_HOST", ConfigModel.base_url)
    llm = OllamaLLM(
        model=model,
        base_url=ollama_host,
    )
    chain = prompt | llm

    predictions = []
    for review in reviews:
        try:
            response = chain.invoke({"text": review})
        except Exception as exc:
            raise RuntimeError(
                f"Failed to reach Ollama at {ollama_host}. Start Ollama or fix the host/port, then retry."
            ) from exc
        label = response.strip().lower()

        if "fake" in label:
            cleaned_label = "fake"
        elif "deceptive" in label:
            cleaned_label = "fake"
        elif "real" in label:
            cleaned_label = "real"
        elif "truthful" in label:
            cleaned_label = "real"
        else:
            cleaned_label = "fake"  # safety fallback
        
        cleaned_label = cleaned_label.strip('.,!?;:')

        #print(f"Raw output: {response} -> Cleaned: {cleaned_label}")
        predictions.append(cleaned_label)

    accuracy, f1, conf_matrix = evaluate_model(df_local, predictions)
    return df_local, predictions, accuracy, f1, conf_matrix


def load_prompt_template(prompt_key, prompt_attr):
    prompt_file = Path(ConfigModel.prompt_file_paths[prompt_key]).resolve()
    spec = importlib.util.spec_from_file_location(f"prompt_{prompt_key}", prompt_file)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load prompt module: {prompt_file}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return getattr(module.Config, prompt_attr)



def save_run_output(df, predictions, output_csv):
    out_df = df.copy()
    out_df["prediction"] = predictions
    out_df.to_csv(output_csv, index=False)


def save_metrics(output_json, model, dataset_path, domain, prompt_type, accuracy, f1, conf_matrix):
    payload = {
        "model": model,
        "dataset": dataset_path,
        "domain": domain,
        "prompt_type": prompt_type,
        "accuracy": accuracy,
        "f1_weighted": f1,
        "confusion_matrix": conf_matrix.tolist(),
    }
    Path(output_json).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def get_available_prompt_attrs(prompt_key):
    return ConfigModel.prompt_templates.get(prompt_key, [])


def main():

    os.environ["OLLAMA_HOST"] = os.environ.get("OLLAMA_HOST", ConfigModel.base_url)
    print(os.environ.get("OLLAMA_HOST"))

    selected_prompt_key = PROMPT_KEY

    for prompt_type in get_available_prompt_attrs(selected_prompt_key):
        for dataset_key, dataset_path in ConfigModel.dataset_paths.items():
            prompt_template = load_prompt_template(prompt_key=selected_prompt_key, prompt_attr=prompt_type)

            df, results, accuracy, f1, conf_matrix = run_prompt_eval(
                dataset_path=dataset_path,
                prompt_template=prompt_template,
                model=ConfigModel.model,
            )

            print("=" * 50)
            print(f"{dataset_key} / {selected_prompt_key} / {prompt_type} Results")
            print(f"Model: {ConfigModel.model}")
            print("=" * 50)
            print("Accuracy:", accuracy)
            print("\nF1 Score:", f1)
            print("\nConfusion Matrix:")
            print(conf_matrix)
            print("=" * 50)

            output_prefix = f"{dataset_key}_{selected_prompt_key}_{prompt_type}"
            save_run_output(df, results, f"{output_prefix}_classified_reviews.csv")
            save_metrics(
                output_json=f"{output_prefix}_results.json",
                model=ConfigModel.model,
                dataset_path=dataset_path,
                domain=dataset_key,
                prompt_type=prompt_type,
                accuracy=accuracy,
                f1=f1,
                conf_matrix=conf_matrix,
            )

if __name__ == "__main__":
    main()