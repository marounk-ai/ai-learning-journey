# process_analyzer.py
# Analyze 5 consulting processes and score them for AI potential
# Week 2 — AI Learning Journey

processes = [
    {
        "name": "KYC document review",
        "industry": "Banking",
        "time_per_case_hours": 4.0,
        "volume_per_month": 500,
        "error_rate_pct": 8,
        "repetitive": True,
    },
    {
        "name": "Regulatory filing preparation",
        "industry": "Banking",
        "time_per_case_hours": 6.0,
        "volume_per_month": 120,
        "error_rate_pct": 5,
        "repetitive": True,
    },
    {
        "name": "Contract clause extraction",
        "industry": "Legal / Consulting",
        "time_per_case_hours": 2.5,
        "volume_per_month": 300,
        "error_rate_pct": 12,
        "repetitive": True,
    },
    {
        "name": "Board report drafting",
        "industry": "Government",
        "time_per_case_hours": 8.0,
        "volume_per_month": 20,
        "error_rate_pct": 3,
        "repetitive": False,
    },
    {
        "name": "RFP response preparation",
        "industry": "Consulting",
        "time_per_case_hours": 12.0,
        "volume_per_month": 15,
        "error_rate_pct": 4,
        "repetitive": False,
    },
]

def score_ai_potential(process):
    """
    Score a process for AI potential on a simple 0-10 scale.
    High volume + high error rate + repetitive = high potential.
    """
    score = 0
    
    # Volume score (0-3)
    if process["volume_per_month"] >= 400:
        score += 3
    elif process["volume_per_month"] >= 100:
        score += 2
    else:
        score += 1
    
    # Error rate score (0-3)
    if process["error_rate_pct"] >= 10:
        score += 3
    elif process["error_rate_pct"] >= 5:
        score += 2
    else:
        score += 1
    
    # Repetitive bonus (0-2)
    if process["repetitive"]:
        score += 2
    
    # Time per case score (0-2)
    if process["time_per_case_hours"] >= 8:
        score += 2
    elif process["time_per_case_hours"] >= 3:
        score += 1
    
    return score

def main():
    print("AI Potential Analysis — Consulting Process Review")
    print("=" * 55)
    
    results = []
    for process in processes:
        score = score_ai_potential(process)
        monthly_hours = process["time_per_case_hours"] * process["volume_per_month"]
        results.append((score, process, monthly_hours))
    
    # Sort by score descending
    results.sort(key=lambda x: x[0], reverse=True)
    
    for rank, (score, process, monthly_hours) in enumerate(results, start=1):
        print(f"\n{rank}. {process['name']} ({process['industry']})")
        print(f"   AI Potential Score : {score}/10")
        print(f"   Monthly volume     : {process['volume_per_month']} cases")
        print(f"   Monthly hours      : {monthly_hours:.0f} hrs")
        print(f"   Error rate         : {process['error_rate_pct']}%")
        print(f"   Repetitive         : {'Yes' if process['repetitive'] else 'No'}")

if __name__ == "__main__":
    main()