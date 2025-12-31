# Evaluation Summary — Week 3

## What you trained
- Model family: Logistic Regression
- Preprocessing:
  - Numerical features: median imputation
  - Categorical features: most-frequent imputation + one-hot encoding
- Key hyperparameters:
  - max_iter = 500

## Results
- Baseline metrics:
  - ROC-AUC ≈ 0.50 (dummy classifier)
- Holdout metrics:
  - ROC-AUC = 1.00
- Confidence intervals:
  - Not computed

## Error analysis
- Worst cases occur for users near the decision threshold.
- Potential target leakage from `total_amount`, which is closely related to the target.
- Small dataset size may inflate performance metrics.

## Recommendation
- Do not ship this model to production yet.
- This model is a strong baseline for comparison.
- Additional data and leakage mitigation are required before deployment.

