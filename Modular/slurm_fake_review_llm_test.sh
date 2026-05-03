#!/bin/bash
#SBATCH --job-name=fake_review_llm_saurac
#SBATCH --partition=gpu-stud
#SBATCH --nodelist=ant1
#SBATCH --gres=gpu:1
#SBATCH --time=06:00:00
#SBATCH --output=job_%j.out
#SBATCH --error=job_%j.err

echo "======================================"
echo "Job started on $(hostname)"
echo "Time: $(date)"
echo "======================================"

# -----------------------------
# CONFIG
# -----------------------------
PORT=11434
OLLAMA_DIR="$HOME/ollama"
MODEL="qwen3.5:9b"
OLLAMA_SIF="ollama_latest.sif"

# -----------------------------
# PREPARE OLLAMA STORAGE
# -----------------------------
mkdir -p "$OLLAMA_DIR"

# -----------------------------
# START OLLAMA SERVER
# -----------------------------
echo "Starting Ollama server..."

apptainer exec --nv \
  --env OLLAMA_HOST=0.0.0.0:$PORT \
  --env OLLAMA_CONTEXT_LENGTH=8192 \
  --bind $OLLAMA_DIR:/root/.ollama \
  $OLLAMA_SIF \
  ollama serve &

OLLAMA_PID=$!

# -----------------------------
# WAIT FOR OLLAMA TO BE READY
# -----------------------------
echo "Waiting for Ollama..."

for i in {1..30}; do
  if curl -s http://localhost:$PORT/api/tags > /dev/null; then
    echo "Ollama is ready!"
    break
  fi
  sleep 2
done

# If still not ready → fail
if ! curl -s http://localhost:$PORT/api/tags > /dev/null; then
  echo "ERROR: Ollama failed to start"
  exit 1
fi

# -----------------------------
# PULL MODEL (ONLY FIRST TIME)
# -----------------------------
echo "Ensuring model is available..."

apptainer exec --nv \
  --env OLLAMA_HOST=0.0.0.0:$PORT \
  --bind $OLLAMA_DIR:/root/.ollama \
  $OLLAMA_SIF \
  ollama pull $MODEL

# -----------------------------
# PYTHON ENV
# -----------------------------
echo "Setting up Python environment..."

# Optional: use venv if you have one
# source $HOME/venv/bin/activate

pip install --user -r requirements.txt

# -----------------------------
# RUN YOUR PIPELINE
# -----------------------------
echo "Running Python pipeline..."

export OLLAMA_BASE_URL="http://localhost:$PORT"

python3 langchain_prompting.py

# -----------------------------
# CLEANUP
# -----------------------------
echo "Stopping Ollama..."

kill $OLLAMA_PID

echo "======================================"
echo "Job finished at $(date)"
echo "======================================"