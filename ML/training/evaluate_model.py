import pandas as pd
import joblib
from sklearn.metrics import classification_report,confusion_matrix,roc_auc_score
df = pd.read_csv("../data/session_data.csv")

features_o= [
    "ip_change", "ua_change", "avg_time_gap",
    "actions_per_min", "session_duration",
    "unique_pages", "geo_distance","time_of_day"
]

X = df[features_o]
y = df["label"]

model =  joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

X_scaled = scaler.transform(X)
pred_raw = model.predict(X_scaled)
y_pred = [1 if p == -1 else 0 for p in pred_raw]


print("📊 Classification Report")
print(classification_report(y, y_pred))

print("📊 Confusion matrix")
print(confusion_matrix(y,y_pred))

print("📊 ROC AUC Score: ",roc_auc_score(y ,y_pred))