import pandas as pd


def run_simulation(scenario):

    df = pd.read_csv("../data/transactions.csv")


    if scenario == "normal":

        return {
            "scenario": "Normal Operation",
            "message": "Liquidity condition is stable",
            "risk_adjustment": 0
        }



    elif scenario == "cash_out_spike":

        provider = "Nagad"

        return {
            "scenario": "Cash-out Spike",
            "provider": provider,
            "message": "Sudden withdrawal pressure detected",
            "risk_adjustment": 45,
            "recommendation": "Increase liquidity monitoring frequency"
        }




    elif scenario == "liquidity_crisis":

        provider = "Nagad"

        return {
            "scenario": "Liquidity Crisis",
            "provider": provider,
            "message": "Cash-out demand significantly exceeds available liquidity",
            "risk_adjustment": 70,
            "recommendation": "Review provider liquidity buffer immediately"
        }



    else:

        return {
            "scenario": "Unknown",
            "message": "No simulation available"
        }
