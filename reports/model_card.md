# Model Card — Week 3 Baseline

## Problem
- Predict: is_high_value for one row per user
- Decision enabled: تحديد المستخدمين اللي يستحقون عرض/حملة خاصة
- Constraints: CPU-only; offline-first; batch inference
- Trained run_id: 2025-12-31T21-49-53Z__classification__seed42

## Data (contract)
- Feature table: data/processed/features.csv
- Unit of analysis: one row per user
- Target column: is_high_value (1 = high value user)
- Optional IDs (passthrough): user_id

## Splits
- Holdout strategy: random split (baseline)
- Leakage risks:
  - total_amount قد يكون قريب من الهدف
  - أي معلومة تُحسب بعد السلوك النهائي للمستخدم

## Metrics
- Primary: ROC-AUC
- Evaluation: holdout split
- Baseline: dummy classifier (majority class)

## Shipping
- Artifacts:
  - Trained model
  - Input schema
  - Evaluation metrics
  - Environment snapshot
- Known limitations:
  - بيانات تجريبية (sample data)
  - عدد مستخدمين قليل
- Monitoring sketch:
  - Distribution of prediction scores
  - Share of predicted high-value users over time

## Reproducibility
- Run id: 2025-12-31T21-49-53Z__classification__seed42
- Git commit: <git rev-parse HEAD>
- Environment: models/runs/2025-12-31T21-49-53Z__classification__seed42/env/pip_freeze.txt
