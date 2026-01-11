def get_sla_rules():
    """
    SLA thresholds per service.
    """
    return {
        "p95_latency_ms": 500, # ≤ 500ms
        "max_error_rate_percent": 2.0,   # ≤ 2%
        "max_avg_cpu": 80.0,  # ≤ 80%
        "max_avg_memory": 85.0 # ≤ 85%
    }
