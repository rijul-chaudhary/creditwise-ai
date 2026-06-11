# Final Feature Treatment Plan

## Feature Treatment Table

| Feature / Feature Group | Treatment Strategy | Reason |
|----------|----------|----------|
| TARGET | Keep | Prediction target variable |
| EXT_SOURCE_1 | Median Imputation + Missing Indicator | Strong predictive power, high missingness |
| EXT_SOURCE_2 | Median Imputation | Strong predictive power, negligible missingness |
| EXT_SOURCE_3 | Median Imputation + Missing Indicator | Strong predictive power, moderate missingness |
| EXT_SOURCE_MEAN | Keep | Strongest correlation discovered during analysis |
| AGE_YEARS | Keep | Engineered feature with predictive value |
| DAYS_BIRTH | Drop after feature creation | Replaced by AGE_YEARS |
| DAYS_EMPLOYED | Replace placeholder values and engineer new feature | Contains invalid placeholder values |
| EMPLOYMENT_YEARS | Under Evaluation | Requires placeholder-value correction before final decision |
| DAYS_EMPLOYED_PLACEHOLDER | Create Indicator Feature | Placeholder values contain useful information |
| AMT_INCOME_TOTAL | Keep | Core financial feature |
| AMT_CREDIT | Keep | Core financial feature |
| AMT_ANNUITY | Median Imputation | Important financial feature with minimal missingness |
| OWN_CAR_AGE | Median Imputation | Potentially useful numeric feature |
| OWN_CAR_AGE_MISSING | Keep | Missingness demonstrated predictive value |
| NAME_CONTRACT_TYPE | One-Hot Encode | Low cardinality |
| CODE_GENDER | One-Hot Encode | Low cardinality |
| FLAG_OWN_CAR | One-Hot Encode | Binary feature |
| FLAG_OWN_REALTY | One-Hot Encode | Binary feature |
| NAME_TYPE_SUITE | Mode Imputation + One-Hot Encode | Low missingness |
| NAME_INCOME_TYPE | One-Hot Encode | Business-relevant feature |
| NAME_EDUCATION_TYPE | One-Hot Encode | Demonstrated predictive value |
| NAME_FAMILY_STATUS | One-Hot Encode | Low cardinality |
| NAME_HOUSING_TYPE | One-Hot Encode | Low cardinality |
| OCCUPATION_TYPE | Fill "Unknown" + One-Hot Encode | Business-relevant feature |
| WEEKDAY_APPR_PROCESS_START | One-Hot Encode | Low cardinality |
| ORGANIZATION_TYPE | Frequency Encoding | High cardinality (58 categories) |
| YEARS_BUILD_* | Drop | Excessive missingness |
| COMMONAREA_* | Drop | Excessive missingness |
| FLOORSMIN_* | Drop | Excessive missingness |
| LIVINGAPARTMENTS_* | Drop | Excessive missingness |
| NONLIVINGAPARTMENTS_* | Drop | Excessive missingness |
| FONDKAPREMONT_MODE | Drop | High missingness |
| HOUSETYPE_MODE | Drop | High missingness |
| WALLSMATERIAL_MODE | Drop | High missingness |
| EMERGENCYSTATE_MODE | Drop | High missingness |