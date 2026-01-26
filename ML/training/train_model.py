import pandas as pd
import joblib 
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

df = pd.read_csv("../data/session_data.csv")

features_o = [
    "ip_change","ua_change","avg_time_gap","actions_per_min",
    "session_duration","unique_pages","geo_distance","time_of_day"
]

#train model on normal behavior
X = df[df["label"] == 0][features_o]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = IsolationForest(n_estimators=300,contamination=0.12,
                        random_state=42)

model.fit(X_scaled)

joblib.dump(model,"model.pkl")
joblib.dump(scaler,"scaler.pkl")

print("✅ Model & Scaler saved successfully")
