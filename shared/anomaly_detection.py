import numpy as np

def detect_anomalies(telemetry, services, z_threshold=3):
    """
    Detect anomalies per service using NumPy.
    """

    service_ids = telemetry["service_id"]
    cpu = telemetry["cpu"]
    memory = telemetry["memory"]
    latency = telemetry["latency"]

    anomalies = {}

    for service in range(1, services + 1):
        mask = service_ids == service

        service_cpu = cpu[mask]
        service_memory = memory[mask]
        service_latency = latency[mask]

        if service_cpu.size == 0:
            continue

        # Z-score calculation (Z-score = How far a value is from normal behavior)
        #Formula: Z = (value − mean) / standard deviation
        cpu_z = (service_cpu - service_cpu.mean()) / service_cpu.std()
        latency_z = (service_latency - service_latency.mean()) / service_latency.std()
        memory_z = (service_memory - service_memory.mean()) / service_memory.std()

        anomalies[service] = {
            "cpu_spikes": int(np.sum(np.abs(cpu_z) > z_threshold)),
            "latency_spikes": int(np.sum(np.abs(latency_z) > z_threshold)),
            "memory_spikes": int(np.sum(np.abs(memory_z) > z_threshold))
        }

    return anomalies
