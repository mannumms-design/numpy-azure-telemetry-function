import numpy as np

def calculate_kpis(telemetry, services):
    """
    Calculate per-service KPIs using NumPy only.
    """
    #Extract array bcz NumPy works best on flat arrays
    service_ids = telemetry["service_id"]
    cpu = telemetry["cpu"]
    memory = telemetry["memory"]
    latency = telemetry["latency"]
    errors = telemetry["errors"]

    results = {}

    #Loop over number of services
    for service in range(1, services + 1):

        # Boolean mask for this service, Example-
        #service_ids = [2, 1, 2, 3]
        #service = 2
        #mask = [True, False, True, False]
        mask = service_ids == service

        service_cpu = cpu[mask]   #i.e. Select only CPU values where mask is True
        service_memory = memory[mask]
        service_latency = latency[mask]
        service_errors = errors[mask]

        if service_cpu.size == 0:
            continue

        results[service] = {
            "request_count": int(service_cpu.size),
            "avg_cpu": float(np.mean(service_cpu)),  #Avg CPU
            "avg_memory": float(np.mean(service_memory)), #float/int for converting NumPy types to Python types
            "p95_latency": float(np.percentile(service_latency, 95)), #P95 Latency for SLA
            "error_rate_percent": float(
                np.mean(service_errors) * 100  #error rate = errors array = [0,1,0,0] Mean = error probability in percentage
            )
        }

    return results
