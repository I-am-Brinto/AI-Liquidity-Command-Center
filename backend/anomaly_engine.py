import pandas as pd


def detect_anomalies():

    df = pd.read_csv("../data/transactions.csv")

    alerts = []

    high_value_limit = 9000

    high_value_transactions = df[
        df["amount"] >= high_value_limit
    ]

    if len(high_value_transactions) > 5:

        alerts.append({
            "alert_type": "Review Required",
            "reason": "Multiple high-value transactions detected",
            "transaction_count": int(len(high_value_transactions)),
            "confidence": 82
        })


    repeated_cash_out = df[
        df["type"] == "cash_out"
    ]

    if len(repeated_cash_out) > 50:

        alerts.append({
            "alert_type": "Review Required",
            "reason": "High cash-out activity detected",
            "transaction_count": int(len(repeated_cash_out)),
            "confidence": 75
        })


    if len(alerts) == 0:

        alerts.append({
            "alert_type": "No Critical Alert",
            "reason": "No unusual pattern detected",
            "transaction_count": 0,
            "confidence": 90
        })


    return alerts
