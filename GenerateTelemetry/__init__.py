#HTTP Trigger Function (NumPy per request)
import json
import azure.functions as func
from shared.telemetry_generator import generate_telemetry
from shared.kpi_analytics import calculate_kpis
from shared.anomaly_detection import detect_anomalies
from shared.sla_rules import get_sla_rules
from shared.sla_detection import detect_sla_breaches

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        records = int(req.params.get("records", 10000))
        services = int(req.params.get("services", 5))

        telemetry = generate_telemetry(records, services)
        kpis = calculate_kpis(telemetry, services)  
        anomalies = detect_anomalies(telemetry, services)
        sla_rules = get_sla_rules()
        sla_breaches = detect_sla_breaches(kpis, sla_rules)

        # Convert NumPy arrays to Python lists for JSON serialization
        # response = {
        #     "records": records,
        #     "services": services,
        #     "sample": {
        #         "service_id": telemetry["service_id"][:10].tolist(),
        #         "cpu": telemetry["cpu"][:10].tolist(),
        #         "memory": telemetry["memory"][:10].tolist(),
        #         "latency": telemetry["latency"][:10].tolist(),
        #         "errors": telemetry["errors"][:10].tolist()
        #     }
        # }
        response = {
            "records": records,
            "services": services,
            "kpis": kpis,
            "anomalies": anomalies,
            "sla_breaches": sla_breaches
        }
 
        return func.HttpResponse(
            json.dumps(response),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=500
        )
