import joblib
import numpy as np
import os
import pandas as pd

# Absolute path based on this file location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "training", "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "..", "training", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

features_o = [
    "ip_change", "ua_change", "avg_time_gap",
    "actions_per_min", "session_duration",
    "unique_pages", "geo_distance","time_of_day"
]

def predict_session(features: dict):
    
    """
    Input: session feature and output will anomaly score and suspicious flag
    
    """
    
    X = pd.DataFrame([features], columns=features_o)

    X_scaled = scaler.transform(X)

    raw_score = model.decision_function(X_scaled)[0]

    anomaly_score = round(
        float(min(max(1 - (raw_score + 0.6), 0), 1)),
        2
    )

    return {
        "anomaly score": anomaly_score,
        "suspicious": bool(anomaly_score >= 0.75)
    }