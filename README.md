*NumPy Telemetry Analytics on Azure (Serverless)

A production-style serverless telemetry analytics system built using Python, NumPy, and Azure Functions, with automated CI/CD using GitHub Actions.

*Project Overview

Modern cloud systems continuously emit telemetry such as CPU usage, memory utilization, request latency, and error rates.
This project simulates that real-world scenario and demonstrates how NumPy can be used for fast analytics inside a cloud-native, serverless architecture.

*Architecture
Client Request
     ↓
Azure Function (HTTP Trigger)
     ↓
NumPy Analytics Engine
     ↓
KPI Metrics + Anomaly Detection + SLA Breach Detection

*Key Features
**Telemetry Generation

Simulates large-scale service telemetry
CPU %, Memory %, Latency (ms), Error counts
Configurable number of services and records

**NumPy KPI Analytics

Mean CPU & memory utilization
P95 latency (real SRE metric)
Error rate per service

**Anomaly Detection

Statistical threshold-based detection
Flags abnormal CPU, memory, or latency spikes

**SLA Breach Detection

Detects latency and error-rate violations
Simulates real production SLA monitoring

**Cloud-Native Deployment

Azure Functions (Python, Linux)
Azure Storage integration
Fully serverless & auto-scaling

**CI/CD Automation

GitHub Actions pipeline
Secure Azure AD Service Principal authentication
Automatic deployment on every push to main

*Tech Stack

Python 3.9
NumPy
Azure Functions
Azure Storage Account
GitHub Actions (CI/CD)
Azure Active Directory (Service Principal)

*Live API Example
GET https://numpy-telemetry-func-hpe4hrcca9fxh4by.centralindia-01.azurewebsites.net/api/telemetry?records=20000&services=5


*Returns:

Aggregated KPIs
Anomaly flags
SLA breach indicators

*Learning Outcomes

Real-world NumPy usage beyond notebooks
Serverless analytics design
Azure Functions internals
CI/CD security best practices
Cloud-scale observability concepts

*Author

Manmohan Tomar
Cloud & AI Enthusiast
