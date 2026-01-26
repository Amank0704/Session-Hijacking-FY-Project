#hybrid and mll boost

def hybrid_decision(ml_score,features):
    rule_score = 0
    if features["ip_change"]:
        rule_score += 0.3
        
    if features["ua_change"]:
        rule_score += 0.2
        
    if features["actions_per_min"] > 40:
        rule_score += 0.3
    
    if features["avg_time_gap"] < 0.5:
        rule_score += 0.2
        
    final_score = round(0.7 * ml_score + 0.3 * rule_score,2)
    
    return{
        "final_score": final_score,
        "is_suspicious" : final_score >= 0.8
    }