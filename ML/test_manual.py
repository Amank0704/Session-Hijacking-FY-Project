from inference.predictor import predict_session

# Normal user behavior
normal = {
    "ip_change": 0,
    "ua_change": 0,
    "avg_time_gap": 5,
    "actions_per_min": 10,
    "session_duration": 40,
    "unique_pages": 6,
    "geo_distance": 0,
    "time_of_day": 0
}

# Attack behavior
attack = {
    "ip_change": 1,
    "ua_change": 1,
    "avg_time_gap": 0.3,
    "actions_per_min": 60,
    "session_duration": 3,
    "unique_pages": 1,
    "geo_distance": 500,
    "time_of_day": 1
}

print("Normal Session:", predict_session(normal))
print("Attack Session:", predict_session(attack))
