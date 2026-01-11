import numpy as np

def generate_telemetry(
    records: int = 100_000,
    services: int = 10
):
    """
    Generate synthetic enterprise telemetry using NumPy.
    """

    service_ids = np.random.randint(1, services + 1, size=records)

    cpu = np.clip(
        np.random.normal(loc=55, scale=15, size=records),
        0, 100
    )

    memory = np.clip(
        np.random.normal(loc=65, scale=20, size=records),
        0, 100
    )

    latency = np.clip(
        np.random.exponential(scale=120, size=records),
        20, 2000
    )

    errors = np.random.binomial(n=1, p=0.02, size=records)

    return {
        "service_id": service_ids,
        "cpu": cpu,
        "memory": memory,
        "latency": latency,
        "errors": errors
    }
