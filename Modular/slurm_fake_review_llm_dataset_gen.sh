#!/bin/bash
#SBATCH --job-name=fake_review_llm_qwen2p5_32b
#SBATCH --partition=gpu-stud
#SBATCH --nodelist=ant2
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem=32G
#SBATCH --time=20:00:00
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
MODEL="qwen2.5:32b"
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

if ! curl -s http://localhost:$PORT/api/tags > /dev/null; then
  echo "ERROR: Ollama failed to start"
  exit 1
fi

# -----------------------------
# PULL MODEL (FIRST TIME ONLY)
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

pip install --user pandas requests tqdm

# -----------------------------
# RUN YOUR GENERATION SCRIPT
# -----------------------------
echo "Running generation pipeline..."

export OLLAMA_HOST="localhost:$PORT"

python3 dataset_gen.py   # <-- your script filename

# -----------------------------
# CLEANUP
# -----------------------------
echo "Stopping Ollama..."

kill $OLLAMA_PID

echo "======================================"
echo "Job finished at $(date)"
echo "======================================"