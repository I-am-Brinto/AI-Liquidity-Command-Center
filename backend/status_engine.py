from liquidity_engine import analyze_liquidity


def get_system_status():

    liquidity = analyze_liquidity()


    highest = max(
        liquidity,
        key=lambda x: x["risk_score"]
    )


    risk = highest["risk_score"]


    if risk >= 70:

        status = "ATTENTION REQUIRED"
        priority = "HIGH"

        action = (
            "Increase liquidity monitoring frequency "
            "and review cash-out pressure"
        )


    elif risk >= 40:

        status = "WARNING"
        priority = "MEDIUM"

        action = (
            "Monitor withdrawal trend "
            "and prepare liquidity response"
        )


    else:

        status = "STABLE"
        priority = "LOW"

        action = (
            "Continue normal operation monitoring"
        )


    return {

        "system_status": status,

        "priority": priority,

        "critical_provider": highest["provider"],

        "risk_score": highest["risk_score"],

        "reason": highest["explanation"],

        "recommended_action": action

    }
