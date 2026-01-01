# Week 3 — Ship-Ready Baseline ML System (Train + Evaluate + Predict)

Turn a feature table into a **reproducible, CPU-friendly ML baseline** with:
- a training command that saves versioned artifacts, and
- a batch prediction command with schema guardrails.

This repo is designed to be:
- **offline-first** (no external services required),
- **reproducible** (run metadata + environment capture),
- **portfolio-ready** (clean structure + model card).

---

## Quickstart

### 1) Setup
```bash
uv sync

### Create sample data
uv run ml-baseline make-sample-data
data/processed/features.csv

###Train a baseline model
uv run ml-baseline train
Training artifacts are saved to:

models/runs/<run_id>/
models/registry/latest.txt (points to the latest trained model)

###  Batch prediction
uv run ml-baseline predict data/processed/features.csv

Predictions are written to the outputs/ directory.
###  Run tests
uv run pytest 

Outputs:

Trained runs: models/runs/
Latest run pointer: models/registry/latest.txt
Evaluation reports: reports/eval_summary.md, reports/model_card.md
Prediction outputs: outputs/



