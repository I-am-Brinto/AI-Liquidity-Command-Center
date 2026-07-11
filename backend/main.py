from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd

from liquidity_engine import analyze_liquidity
from anomaly_engine import detect_anomalies
from simulation_engine import run_simulation
from metrics_engine import get_metrics
from status_engine import get_system_status

app = FastAPI(
    title="Super Agent Liquidity Intelligence API",
    description="Synthetic operational intelligence platform",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



class SimulationRequest(BaseModel):
    scenario: str



@app.get("/")
def home():

    return {
        "message": "Super Agent API Running",
        "status": "healthy"
    }



@app.get("/transactions")
def get_transactions():

    df = pd.read_csv("../data/transactions.csv")

    return df.to_dict(orient="records")



@app.get("/liquidity")
def get_liquidity():

    return analyze_liquidity()



@app.get("/alerts")
def get_alerts():

    return detect_anomalies()



@app.post("/simulate")
def simulate(request: SimulationRequest):

    return run_simulation(request.scenario)



@app.get("/metrics")
def metrics():

    return get_metrics()


@app.get("/status")
def status():

    return get_system_status()
