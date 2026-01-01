# Week 3 — Ship-Ready Baseline ML System (Train + Evaluate + Predict)

Turn a feature table into a reproducible, CPU-friendly machine learning baseline that supports training, evaluation, and batch prediction.

This project is designed to be:
- offline-first (no external services required)
- reproducible (saved run metadata and artifacts)
- suitable for academic evaluation and portfolio presentation

---

## Quickstart

### 1) Setup
Install all required dependencies.
Command:
- uv sync

### 2) Create sample data
Generate a small processed feature table used for training and prediction.
Command:
- uv run ml-baseline make-sample-data
Output:
- data/processed/features.csv

### 3) Train a baseline model
Train a baseline classification model (requires specifying the target column).
Command:
- uv run ml-baseline train --target is_high_value
Outputs:
- models/runs/<run_id>/
- models/registry/latest.txt (points to the latest trained model)
- reports/eval_summary.md
- reports/model_card.md

### 4) Batch prediction
Run batch predictions using the saved run.
Command:
- uv run ml-baseline predict data/processed/features.csv
Output:
- outputs/

### 5) Run tests
Run automated tests to verify training/prediction and schema validation.
Command:
- uv run pytest
