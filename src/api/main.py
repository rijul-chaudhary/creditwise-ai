from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load models
BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODELS_DIR = BASE_DIR / "models"

loaded_lgbm = joblib.load(
    MODELS_DIR / "lightgbm_final.pkl"
)

loaded_xgb = joblib.load(
    MODELS_DIR / "xgboost_final.pkl"
)

feature_columns = joblib.load(
    MODELS_DIR / "feature_columns.pkl"
)

app = FastAPI(
    title="CreditWise AI",
    description="Loan Default Risk Prediction API",
    version="1.0"
)

class PredictionRequest(BaseModel):
    strategy: str = "balanced"
    features: dict

class PredictionResponse(BaseModel):
    probability: float
    risk_score: float
    risk_category: str
    strategy: str

def generate_risk_score(probability):
    return round(probability * 100, 2)

def get_risk_category(probability, strategy="balanced"):

    strategy_thresholds = {
        "risk_sensitive": 0.50,
        "balanced": 0.55,
        "performance_optimized": 0.60
    }

    threshold = strategy_thresholds[strategy]

    if probability >= threshold:
        return "High Risk"
    elif probability >= threshold * 0.6:
        return "Medium Risk"
    else:
        return "Low Risk"

def predict_customer_risk(customer_data, strategy="balanced"):

    lgbm_prob = loaded_lgbm.predict_proba(
        customer_data
    )[:, 1][0]

    xgb_prob = loaded_xgb.predict_proba(
        customer_data
    )[:, 1][0]

    probability = (
        lgbm_prob + xgb_prob
    ) / 2

    risk_score = generate_risk_score(
        probability
    )

    risk_category = get_risk_category(
        probability,
        strategy
    )

    return {
        "probability": round(float(probability), 4),
        "risk_score": float(risk_score),
        "risk_category": risk_category,
        "strategy": strategy
    }

@app.get("/")
def home():
    return {
        "message": "CreditWise AI API Running"
    }

@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(request: PredictionRequest):

    customer_df = pd.DataFrame(
        [request.features]
    )

    customer_df = customer_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    return predict_customer_risk(
        customer_df,
        strategy=request.strategy
    )
