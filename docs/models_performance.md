# Final Model Performance Comparison

The following models were evaluated throughout the project to identify the most effective approach for predicting loan default risk. Performance was assessed primarily using **ROC-AUC**, which measures a model's ability to distinguish between defaulters and non-defaulters across all classification thresholds. Additional metrics such as precision, recall, and F1-score for the default class were also considered due to the highly imbalanced nature of the dataset.

| Model | ROC-AUC | Precision | Recall | F1-Score |
|---------|---------:|---------:|---------:|---------:|
| Logistic Regression | 0.7486 | 0.58 | 0.01 | 0.02 |
| Balanced Logistic Regression | 0.7482 | 0.16 | 0.68 | 0.26 |
| XGBoost | 0.7595 | 0.17 | 0.66 | 0.28 |
| LightGBM | 0.7596 | 0.17 | 0.67 | 0.28 |
| XGBoost (Without SK_ID_CURR) | 0.7586 | 0.18 | 0.64 | 0.28 |
| LightGBM (Without SK_ID_CURR) | 0.7600 | 0.17 | 0.67 | 0.27 |
| **LightGBM + XGBoost Ensemble** | **0.7604** | **0.18** | **0.66** | **0.28** |

## Model Development Summary

### Logistic Regression Baseline
A standard Logistic Regression model was used as the initial benchmark. While it achieved a reasonable ROC-AUC score, it failed to identify default cases effectively due to the severe class imbalance present in the dataset.

### Balanced Logistic Regression
Applying class weighting significantly improved recall for the minority class, enabling the model to detect a much larger proportion of defaulters. This highlighted the importance of addressing class imbalance in credit-risk prediction problems.

### Gradient Boosting Models
XGBoost and LightGBM were subsequently trained to capture complex non-linear relationships between applicant characteristics and loan default behaviour. Both models outperformed the logistic regression baselines and demonstrated substantially stronger predictive capability.

### Feature Engineering Impact
Several engineered features emerged as highly influential predictors, including:

- `EXT_SOURCE_MEAN`
- `AGE_YEARS`
- `EMPLOYMENT_YEARS`
- `EXT_SOURCE_1_MISSING`
- `OWN_CAR_AGE_MISSING`
- `ORGANIZATION_TYPE_FREQ`

The importance of these variables confirms that feature engineering and missing-value treatment contributed meaningfully to model performance.

### Identifier Validation
Feature importance analysis revealed that `SK_ID_CURR` appeared among the influential features in some models. Since customer identifiers should not contain predictive information, additional validation experiments were conducted.

Both LightGBM and XGBoost were retrained after removing the identifier. Performance remained largely unchanged, confirming that the models were learning from meaningful customer attributes rather than relying on dataset-specific identifiers.

### Ensemble Modeling
Finally, a probability-averaging ensemble combining LightGBM and XGBoost was constructed. The ensemble achieved the highest ROC-AUC score among all evaluated approaches while maintaining strong recall for the default class.

---

# Final Selected Model

## LightGBM + XGBoost Ensemble

### Performance

| Metric | Value |
|----------|----------:|
| ROC-AUC | **0.7604** |
| Precision | **0.18** |
| Recall | **0.66** |
| F1-Score | **0.28** |

### Reason for Selection

The LightGBM + XGBoost Ensemble was selected as the final model because it:

- Achieved the highest ROC-AUC score among all evaluated models.
- Combined the strengths of the two best-performing gradient boosting algorithms.
- Maintained strong default-detection capability on an imbalanced dataset.
- Demonstrated robustness after removal of identifier-based features.
- Leveraged engineered features and domain-informed preprocessing strategies developed throughout the project.
- Represents a practical and production-ready approach for credit-risk prediction.

### Conclusion

The final ensemble model successfully balances predictive performance, robustness, and interpretability, making it the strongest candidate for deployment within the CreditWise AI credit-risk assessment system.