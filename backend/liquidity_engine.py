import pandas as pd


def analyze_liquidity():

    df = pd.read_csv("../data/transactions.csv")

    results = []

    for provider in df["provider"].unique():

        provider_data = df[df["provider"] == provider]

        total_cash_out = provider_data[
            provider_data["type"] == "cash_out"
        ]["amount"].sum()

        total_cash_in = provider_data[
            provider_data["type"] == "cash_in"
        ]["amount"].sum()

        transaction_count = len(provider_data)

        pressure = total_cash_out / (total_cash_in + 1)

        risk_score = min(round(float(pressure * 50), 2), 95)

        if risk_score > 60:
            status = "High Risk"
            reason = "Cash-out demand is higher than incoming liquidity"

        elif risk_score > 30:
            status = "Medium Risk"
            reason = "Increasing withdrawal pressure detected"

        else:
            status = "Low Risk"
            reason = "Liquidity condition is stable"


        results.append({
            "provider": provider,
            "cash_in": int(total_cash_in),
            "cash_out": int(total_cash_out),
            "transactions": int(transaction_count),
            "risk_score": float(risk_score),
            "status": status,
            "explanation": reason
        })


    return results
