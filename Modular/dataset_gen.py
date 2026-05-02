import os
import requests
import pandas as pd
from tqdm import tqdm
import re
import time

# -----------------------------
# CONFIG
# -----------------------------
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost:11434")
OLLAMA_URL = f"http://{OLLAMA_HOST}/api/generate"

MODEL = "qwen2.5:32b"

INPUT_PATH = "/home/sohy47ma/ReviewProject_new/fake_reviews_prediction/Datasets/Hotel_Human_VS_HumanFake.csv"
OUTPUT_PATH = "/home/sohy47ma/ReviewProject_new/fake_reviews_prediction/Datasets/Hotel_CG_Reviews_final.csv"

NUM_PER_HOTEL = 40   # increase if needed
MAX_RETRIES = 3

# -----------------------------
# PROMPTS
# -----------------------------
SYSTEM_PROMPT = (
    "You write realistic hotel reviews. "
    "The reviews should look like genuine user opinions for analysis of fake-review detectors. "
    "Do not mention that you are an AI or that this is synthetic."
)

def generate_with_ollama(model: str, system_prompt: str, user_prompt: str) -> str:
    payload = {
        "model": model,
        "system": system_prompt,
        "prompt": user_prompt,
        "stream": False
    }

    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.post(OLLAMA_URL, json=payload, timeout=300)
            resp.raise_for_status()
            text = resp.json()["response"]

            # Remove any <thought>...</thought> blocks
            text = re.sub(r"<thought>.*?</thought>\s*", "", text, flags=re.S)

            return text.strip().strip('"')

        except Exception as e:
            print(f"[WARN] Request failed (attempt {attempt+1}): {e}")
            time.sleep(2)

    return "Failed to generate review."

# -----------------------------
# MAIN PIPELINE
# -----------------------------
def main():
    print(f"Using Ollama at: {OLLAMA_URL}")
    print(f"Model: {MODEL}")

    df = pd.read_csv(INPUT_PATH)
    unique_hotels = df["Category"].unique()

    generated_rows = []

    for hotel in tqdm(unique_hotels, desc="Generating reviews"):
        for _ in range(NUM_PER_HOTEL):
            user_prompt = (
                f"Write a hotel review for '{hotel}'. "
                f"Include comments about location, cleanliness, staff, and overall experience. "
                f"Length: 2–3 sentences."
            )

            text = generate_with_ollama(MODEL, SYSTEM_PROMPT, user_prompt)

            generated_rows.append({
                "Binary_label": "fake",
                "Category": hotel,
                "domain": "Hotel",
                "text": text,
                "is_synthetic": 1,
                "source": MODEL,
            })

    df_out = pd.DataFrame(generated_rows)

    df_out.to_csv(OUTPUT_PATH, index=False)

    print("======================================")
    print("Saved generated reviews to:", OUTPUT_PATH)
    print("Total rows:", len(df_out))
    print("======================================")

# -----------------------------
# ENTRY
# -----------------------------
if __name__ == "__main__":
    main()