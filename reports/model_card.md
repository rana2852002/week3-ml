# Model Card — Week 3 Baseline

## Problem
- Predict: is_high_value for one row per user
- Decision enabled: تحديد المستخدمين اللي يستحقون عرض/حملة خاصة
- Constraints: CPU-only; offline-first; batch inference

## Data (contract)
- Feature table: data/processed/features.csv
- Unit of analysis: one row per user
- Target column: is_high_value (1 = high value user)
- Optional IDs (passthrough): user_id

## Splits (draft)
- Holdout strategy: random split (baseline)
- Leakage risks:
  - total_amount قد يكون قريب من الهدف
  - أي معلومة تُحسب بعد سلوك المستخدم النهائي

## Metrics (draft)
- Primary: ROC-AUC
- Baseline: dummy classifier (majority class)

## Shipping
- Artifacts: trained model, schema, metrics, environment snapshot
- Known limitations:
  - بيانات تجريبية (sample data)
  - عدد مستخدمين قليل
- Monitoring sketch:
  - توزيع التوقعات
  - نسبة high value users
