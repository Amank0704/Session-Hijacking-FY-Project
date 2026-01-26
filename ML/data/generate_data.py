import pandas as pd 
import numpy as np

np.random.seed(42)

def generate_data(samples = 3000):      #2250 normal and 750 attack
    rows = []
    
    for _ in range(samples):
        attack = np.random.choice([0,1],p=[0.75,0.25])
        rows.append({
            "ip_change": int(attack),
            "ua_change": int(attack),
            "avg_time_gap":np.random.uniform(0.2,1.0) if attack else np.random.uniform(2,12),
            "actions_per_min": np.random.randint(40, 80) if attack else np.random.randint(4, 18),
            "session_duration": np.random.uniform(2, 6) if attack else np.random.uniform(15, 90),
            "unique_pages": np.random.randint(1, 2) if attack else np.random.randint(3, 10),
            "geo_distance": np.random.uniform(200, 900) if attack else 0,
            "time_of_day": np.random.choice([0, 1], p=[0.3, 0.7]) if attack else np.random.choice([0, 1], p=[0.85, 0.15]),
            "label": attack
        })
    df = pd.DataFrame(rows)
    df.to_csv("session_data.csv",index = False)
    print("✅ Dataset generated: session_data.csv")

generate_data()    


    