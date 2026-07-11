import pandas as pd

def get_metrics():
    df = pd.read_csv("../data/transactions.csv")

    total_transactions = len(df)

    total_cash_in = df[df["type"]=="cash_in"]["amount"].sum()
    total_cash_out = df[df["type"]=="cash_out"]["amount"].sum()

    # simple risk metric
    risk = abs(total_cash_out - total_cash_in) / (total_cash_in + 1) * 100

    return {
        "transactions": int(total_transactions),
        "cash_in": int(total_cash_in),
        "cash_out": int(total_cash_out),
        "risk_score": round(float(risk),2),
        "status": "High Risk" if risk>60 else "Stable"
    }
