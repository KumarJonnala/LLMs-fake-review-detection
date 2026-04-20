# Modular Workflow (ANTs + Ollama + Slurm)

This README explains how to run the Modular pipeline on ANTs with Ollama.

## 1) What is in this folder

- `config_model.py`: model, Ollama host, dataset map, prompt file map, prompt-template map.
- `langchain_prompting.py`: main runner (loads selected prompt version and templates, evaluates across datasets, saves CSV/JSON outputs).
- `slurm_fake_review_llm.sh`: batch script entrypoint.
- `requirements.txt`: Python dependencies.
- `AntsCluster.txt`: cluster notes/commands.

## 2) Connect and prepare

```bash
ssh username@ants.cs.ovgu.de
cd /home/username/directory

```

## 3) Request a GPU node

Use a partition/group your account is allowed to use.

```bash
srun -p gpu-stud -w ant2 --gres=shard:8 --pty bash
```

Important: start Ollama and run Python on the same node.

## 4) Start Ollama (same node)

If needed:

```bash
apptainer pull ollama.sif docker://ollama/ollama
mkdir -p "$HOME/ollama"
```

Start server:

```bash
apptainer exec --nv \
  --env OLLAMA_HOST=0.0.0.0:xxxxx \
  --bind $HOME/ollama:/root/.ollama \
  ollama.sif \
  ollama serve
```

Validate service and model:

```bash
apptainer exec --nv \
  --env OLLAMA_HOST=0.0.0.0:xxxxx \
  ollama.sif \
  ollama list

apptainer exec --nv \
  --env OLLAMA_HOST=0.0.0.0:xxxxx \
  --bind "$HOME/ollama:/root/.ollama" \
  ollama.sif \
  ollama pull gemma3:12b
```

## 5) Configure run behavior

Edit `config_model.py`:

- `base_url` should match Ollama server endpoint (for this setup: `http://localhost:xxxxx`).
- `model` should be available in Ollama (for example `gemma3:12b`).
- `dataset_paths`, `prompt_file_paths`, and `prompt_templates` control what runs.

Edit `langchain_prompting.py`:

- `PROMPT_KEY = "ver_1"` selects one prompt version.
- Script runs all templates listed under `prompt_templates[PROMPT_KEY]` across all datasets in `dataset_paths`.

## 6) Run directly (interactive)

```bash
python3 langchain_prompting.py
```

Outputs are generated per dataset/template pair:

- `<dataset>_<prompt_key>_<prompt_type>_classified_reviews.csv`
- `<dataset>_<prompt_key>_<prompt_type>_results.json`

## 7) Submit via Slurm

```bash
sbatch slurm_fake_review_llm.sh
squeue
```

Cancel if needed:

```bash
scancel <jobid>
```

## 8) Recommended Slurm pattern

To avoid connection issues, ensure Ollama is started inside the same Slurm job before Python execution. If Ollama is on a different node, `localhost` will fail with connection refused.