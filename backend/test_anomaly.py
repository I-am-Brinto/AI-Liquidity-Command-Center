from anomaly_engine import detect_anomalies

result = detect_anomalies()

for alert in result:
    print(alert)
