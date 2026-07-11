const API = "http://127.0.0.1:8000";


async function loadDashboard() {


    const [
        liquidityData,
        alertData,
        metricsData,
        statusData
    ] = await Promise.all([

        fetch(`${API}/liquidity`).then(r=>r.json()),

        fetch(`${API}/alerts`).then(r=>r.json()),

        fetch(`${API}/metrics`).then(r=>r.json()),

        fetch(`${API}/status`).then(r=>r.json())

    ]);




    // KPI CARDS

    document.getElementById("transactionCount").innerText =
        metricsData.transactions;


    document.getElementById("cashFlow").innerText =
        metricsData.cash_in + metricsData.cash_out;


    document.getElementById("overallRisk").innerText =
        metricsData.risk_score + "%";


    document.getElementById("systemStatus").innerText =
        statusData.system_status;



    // AI SYSTEM STATUS


    document.getElementById("systemStatusPanel").innerHTML = `


    <h3>
    AI Decision Engine
    </h3>


    <p>
    Status:
    <b>${statusData.system_status}</b>
    </p>


    <p>
    Priority:
    <b>${statusData.priority}</b>
    </p>


    <p>
    Critical Provider:
    <b>${statusData.critical_provider}</b>
    </p>


    <p>
    Risk Score:
    <b>${statusData.risk_score}%</b>
    </p>


    <p>
    Reason:
    ${statusData.reason}
    </p>


    <p>
    Recommended Action:
    ${statusData.recommended_action}
    </p>


    `;






    // PROVIDERS


    const providerDiv =
    document.getElementById("providers");


    providerDiv.innerHTML="";



    liquidityData.forEach(provider=>{


        let riskColor =
        provider.risk_score >=70
        ?
        "#ef4444"
        :
        provider.risk_score >=40
        ?
        "#facc15"
        :
        "#22c55e";



        providerDiv.innerHTML += `


        <div class="provider-card">


        <h2>
        ${provider.provider}
        </h2>


        <div class="risk">
        ${provider.risk_score}%
        </div>



        <div style="
        background:#334155;
        height:10px;
        border-radius:10px;">


        <div style="
        width:${provider.risk_score}%;
        height:10px;
        background:${riskColor};
        border-radius:10px;">
        </div>


        </div>



        <p>
        Status:
        <b>${provider.status}</b>
        </p>


        <p>
        Cash In:
        ${provider.cash_in}
        </p>


        <p>
        Cash Out:
        ${provider.cash_out}
        </p>



        <p class="explanation">
        AI Explanation:
        ${provider.explanation}
        </p>



        <p class="explanation">
        AI Recommendation:
        ${
        provider.risk_score>=70
        ?
        "Increase liquidity monitoring frequency"
        :
        "Continue normal monitoring"
        }
        </p>


        </div>


        `;


    });








    // AI EXECUTIVE INSIGHT


    document.getElementById("insight").innerHTML = `


    <h3>
    AI Executive Summary
    </h3>


    <p>
    Overall:
    <b>${statusData.system_status}</b>
    </p>


    <p>
    Critical Provider:
    <b>${statusData.critical_provider}</b>
    </p>


    <p>
    Risk:
    <b>${statusData.risk_score}%</b>
    </p>


    <p>
    Action:
    ${statusData.recommended_action}
    </p>


    `;






    // COMPARISON


    const comparison =
    document.getElementById("comparison");


    comparison.innerHTML="";


    liquidityData.forEach(provider=>{


        comparison.innerHTML += `


        <div style="margin:15px 0">


        <b>
        ${provider.provider}
        </b>


        <div style="
        background:#334155;
        height:18px;
        border-radius:10px;">


        <div style="
        width:${provider.risk_score}%;
        height:18px;
        background:#38bdf8;
        border-radius:10px;">
        </div>


        </div>


        </div>


        `;


    });






    // ALERTS


    const alertDiv =
    document.getElementById("alerts");


    alertDiv.innerHTML="";



    alertData.forEach(alert=>{


        alertDiv.innerHTML += `


        <div class="alert-card">


        <h3>
        [!] ${alert.alert_type}
        </h3>


        <p>
        ${alert.reason}
        </p>


        <p>
        Transactions:
        ${alert.transaction_count}
        </p>


        <p class="confidence">
        Confidence:
        ${alert.confidence}%
        </p>


        </div>


        `;


    });



}






async function runSimulation(){


    const scenario =
    document.getElementById("scenario").value;



    const response =
    await fetch(`${API}/simulate`,
    {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },


        body:JSON.stringify({
            scenario:scenario
        })

    });



    const data =
    await response.json();



    document.getElementById("simulationResult").innerHTML = `


    <h3>
    Simulation Result
    </h3>


    <p>
    Scenario:
    <b>${data.scenario}</b>
    </p>


    <p>
    Provider:
    <b>${data.provider || "All"}</b>
    </p>


    <p>
    Risk Impact:
    <b>+${data.risk_adjustment || 0}%</b>
    </p>


    <p>
    ${data.message}
    </p>


    <p>
    Recommendation:
    ${data.recommendation || ""}
    </p>


    `;

}



loadDashboard();
