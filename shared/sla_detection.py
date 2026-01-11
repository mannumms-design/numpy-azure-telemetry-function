def detect_sla_breaches(kpis, sla_rules):
    """
    Detect SLA breaches based on computed KPIs.
    """

    breaches = {}

    for service_id, metrics in kpis.items():
        service_breaches = []

        if metrics["p95_latency"] > sla_rules["p95_latency_ms"]:
            service_breaches.append("P95 latency SLA breached")

        if metrics["error_rate_percent"] > sla_rules["max_error_rate_percent"]:
            service_breaches.append("Error rate SLA breached")

        if metrics["avg_cpu"] > sla_rules["max_avg_cpu"]:
            service_breaches.append("Average CPU SLA breached")

        if metrics["avg_memory"] > sla_rules["max_avg_memory"]:
            service_breaches.append("Average memory SLA breached")

        if service_breaches:
            breaches[service_id] = service_breaches

    return breaches
