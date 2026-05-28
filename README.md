# Overview

This document describes the code, the primary datasets used by the RAG pipelines, and the exact dependency files required to run the code.

**Purpose**
- **Backup_Files:** Contains code for the initial testing purposes (Not used currently).
- **Datasets:** All the datasets used.
- **Modular:** Utilities and prompt-driven evaluation helpers for running single-model prompt evaluations and saving metrics.
- **Modular_RAG:** Multi-dataset, multi-model RAG evaluation drivers using FAISS, HuggingFace embeddings, and Ollama-based LLMs.
- **Paper_for_proof:** Reference papers.

**Key files (entry points)**
- **Modular prompt runner:** [Modular/langchain_prompting.py](Modular/langchain_prompting.py#L1-L20) — runs prompt templates against a dataset using `OllamaLLM` and saves predictions/metrics.
- **RAG driver:** [Modular_RAG/RAG.py](Modular_RAG/RAG.py#L1-L30) — dataset × model evaluation loop, builds a FAISS vectorstore, retrieves examples, and scores models.
- **Notebook-derived runner:** [curren_files/RAG_new.py](curren_files/RAG_new.py#L1-L30) — a converted notebook variant of a RAG evaluation flow useful for quick experiments.

**Datasets referenced**
- [Datasets/Hotel_HumanReal_VS_CG_32B_Model.csv](Datasets/Hotel_HumanReal_VS_CG_32B_Model.csv#L60-L66) — balanced real vs CG hotel reviews used for RAG evaluation/experiments.
- [Datasets/Amazon_Human_VS_ComputerFake.csv](Datasets/Amazon_Human_VS_ComputerFake.csv#L30-L36) — Amazon human vs synthetic dataset used in experiments and examples.
- [Datasets/Hotel_Human_VS_HumanFake_relabelled.csv](Datasets/Hotel_Human_VS_HumanFake_relabelled.csv) — Human written fake and real reviews of hotels and examples dataset used in experiments and examples.
- [Datasets/Hotel_HumanReal_VS_MixFake.csv](Datasets/Hotel_HumanReal_VS_MixFake.csv) — Human written real hotel reviews and Mix fake (consits of human written fake and computer generated review) dataset used in experiments and examples.

- [Datasets/Hotel_HumanReal_VS_CG.csv](Datasets/Hotel_HumanReal_VS_CG.csv) — Human written real hotel reviews and Computer genrated hotel reviews dataset used in experiments and examples.



If you plan to run the RAG scripts, ensure the CSVs exist at the paths expected by the drivers or update `DATASETS` / `CSV_PATH` in the scripts.

**Dependency files (exact manifests)**
- [Modular/requirements.txt](Modular/requirements.txt#L1-L7)
- [Modular_RAG/requirements.txt](Modular_RAG/requirements.txt#L1-L8)

The manifests contain the core Python packages required. Example entries include `pandas`, `scikit-learn`, `langchain-core`, `langchain-community`, and `langchain-ollama`. `Modular_RAG/requirements.txt` also lists `faiss-cpu` and `sentence-transformers` for embeddings and vector store support.

**Quick setup**
1. Create and activate a virtualenv (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies (either one or both manifests as needed):

```bash
pip install -r Modular/requirements.txt
pip install -r Modular_RAG/requirements.txt
```

3. Set the Ollama host (if using Ollama):

```bash
export OLLAMA_HOST=http://localhost:8500
```
4. To download the latest ollama image in HPC cluster run in the root directory.
```bash
apptainer pull ollama_latest.sif docker://ollama/ollama
```
This will install a package file for ollama.that will be used when running slurm job.
**Run examples**
- To run the modular prompt evaluator (uses `ConfigModel` and configured prompts):

```bash
python Modular/langchain_prompting.py
```

- To run the RAG evaluation driver (builds FAISS vectorstore and evaluates models listed in the script):

```bash
python Modular_RAG/RAG.py
```

Notes:
- The RAG driver saves a local FAISS vectorstore to `VECTORSTORE_PATH` (variable in the script). If you re-run multiple datasets, the vectorstore may be overwritten — set a unique path or persist between runs as needed.
- Ollama-based LLM calls assume an Ollama server/daemon reachable at `OLLAMA_HOST`; if Ollama is not used, adapt code to your preferred LLM wrapper.
- `faiss-cpu` may require platform-specific wheels — on macOS use pip with compatible versions or build from source if necessary.

**Slurm Workflows**
- The repository includes Slurm job scripts for running experiments on an HPC/GPU cluster. Each script configures resources, optionally starts an Ollama server inside an Apptainer container, installs Python dependencies, runs the pipeline, then performs cleanup.

Available job scripts:
- [Modular/slurm_fake_review_llm.sh](Modular/slurm_fake_review_llm.sh#L1-L12) — basic Slurm job that runs `langchain_prompting.py` (GPU partition, simple install).
- [Modular/slurm_fake_review_llm_gemma.sh](Modular/slurm_fake_review_llm_gemma.sh#L1-L20) — starts Ollama (Apptainer), pulls `gemma3:27b`, installs deps, runs `langchain_prompting.py`, then kills Ollama. Suitable for long runs and large models.
- [Modular/slurm_fake_review_llm_llama.sh](Modular/slurm_fake_review_llm_llama.sh#L1-L20) — similar to the gemma script but configured for `llama3:8b` (adjusts `OLLAMA_CONTEXT_LENGTH`).
- [Modular/slurm_fake_review_llm_phi4.sh](Modular/slurm_fake_review_llm_phi4.sh#L1-L20) — starts Ollama and pulls `phi4:14b` before running the pipeline.
- [Modular/slurm_fake_review_llm_dataset_gen.sh](Modular/slurm_fake_review_llm_dataset_gen.sh#L1-L20) — runs a dataset generation pipeline (starts Ollama, runs `dataset_gen.py`).
- [Modular/slurm_fake_review_llm_test.sh](Modular/slurm_fake_review_llm_test.sh#L1-L20) — test job for smaller models (`qwen3.5:9b`) and quick verification.
- [Modular_RAG/slurm_fake_reviews_prediction.sh](Modular_RAG/slurm_fake_reviews_prediction.sh#L1-L12) — Slurm wrapper to run the RAG evaluation (`RAG_new.py`) with resource requests tuned for vectorstore builds.

Example submit command:

```bash
sbatch Modular/slurm_fake_review_llm_gemma.sh
```

Key notes when using these scripts:
- They use `apptainer` to run an Ollama SIF image and bind a host directory for model storage (`$HOME/ollama`). Ensure `apptainer` and the SIF image (e.g., `ollama_latest.sif`) are available on the cluster.
- Scripts wait for Ollama to respond on the configured port before pulling models and running Python code.
- Resource requests (`--gres=gpu`, `--cpus-per-gpu`, `--mem`, `--time`) are conservative examples — adjust to your cluster's configuration and model size.
- Logs are written to `job_%j.out` / `job_%j.err` in the working directory by default.
- If your cluster restricts outbound network access or container execution, adapt the scripts to use a pre-loaded model directory and skip `ollama pull`.

