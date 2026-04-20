#!/bin/bash
#SBATCH --job-name=fake_review_llm
#SBATCH --partition=gpu
#SBATCH --nodelist=ant2
#SBATCH --output=job_%j.out
#SBATCH --error=job_%j.err

#SBATCH --gres=shard:8
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G
#SBATCH --time=06:00:00

pip install -r requirements.txt
python3 langchain_prompting.py