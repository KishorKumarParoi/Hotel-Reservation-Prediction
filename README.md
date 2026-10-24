# 🏨 Hotel Reservation Cancellation Prediction - Enterprise MLOps Platform

[![Architecture Flow](docs/images/01_architecture_flow.svg)](docs/images/01_architecture_flow.svg)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)](https://mlflow.org/)
[![Accuracy](https://img.shields.io/badge/Test_Accuracy-89.11%25-brightgreen?style=for-the-badge)](ARCHITECTURE.md)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

A production-grade, end-to-end Machine Learning system engineered according to the **Enterprise AI Architect Roadmap (Phases 0 - 5)**. Predicts customer booking cancellations with **89.11% test accuracy** and **<15ms P95 latency**.

---

## ⚡ One-Click Cloud Bootstrap (Zero-Touch)

Deploy the complete platform on any Ubuntu, Debian, AWS EC2, GCP Compute Engine, or macOS instance with a single command:

```bash
curl -fsSL https://raw.githubusercontent.com/KishorKumarParoi/Hotel-Reservation-Prediction/main/bootstrap.sh | bash
```

This single command automatically installs system dependencies, clones the repository, builds the optimized Docker container, and launches the prediction service with health checks.

---

## 🚀 Quick Start & Deployment Options

Clone and launch locally using the unified `deploy.sh` script:

```bash
git clone https://github.com/KishorKumarParoi/Hotel-Reservation-Prediction.git
cd Hotel-Reservation-Prediction
chmod +x deploy.sh clear.sh bootstrap.sh
```

### 1. Docker Compose Mode (Default)
```bash
./deploy.sh
```
*Builds and runs the web prediction service with automated health validation.*

### 2. Standalone Container Mode
```bash
./deploy.sh --quick
```

### 3. Native Host Execution
```bash
./deploy.sh --host
```

---

## 🧹 Zero-Cost Teardown ($0.00 Spend)

To cleanly terminate all running containers, networks, and background processes with zero residue:

```bash
./clear.sh
```

---

## 📡 API Reference & Integration

### 1. Health Probe
```bash
curl -s http://localhost:8080/health | jq .
```
**Response:**
```json
{
  "model_loaded": true,
  "model_path": "artifacts/models/lgbm_model.pkl",
  "service": "hotel-reservation-prediction",
  "status": "ok"
}
```

### 2. Real-Time Reservation Cancellation Prediction
```bash
curl -s -X POST http://localhost:8080/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "lead_time": 45,
    "no_of_special_requests": 1,
    "avg_price_per_room": 115.0,
    "arrival_month": 7,
    "arrival_date": 20,
    "market_segment_type": 4,
    "no_of_week_nights": 3,
    "no_of_weekend_nights": 2,
    "type_of_meal_plan": 0,
    "room_type_reserved": 0
  }' | jq .
```
**Response:**
```json
{
  "confidence": 0.8911,
  "interpretation": "Will Not Cancel",
  "prediction": 1,
  "status": "success"
}
```

### 3. Prometheus Metrics
```bash
curl -s http://localhost:8080/metrics
```

---

## 🏗️ Architecture & Technical Specifications

For full architectural blueprints, mathematical derivations of gradient boosting, schema definitions, and trade-off analyses, please consult [ARCHITECTURE.md](ARCHITECTURE.md).

```
+----------------------------------------------------------------------------------------------------+
|                                    ENTERPRISE ARCHITECTURE FLOW                                    |
+----------------------------------------------------------------------------------------------------+
 [ Raw Ingestion ]            [ Feature Pipeline ]                  [ Real-Time Serving ]
 36,275 Records (S3/GCS) ---> Categorical & Skewness Pipeline ----> Flask REST API (:8080)
                              Top 10 Feature Attributes             P95 Latency < 15ms
                                          |                                  ^
                                          v                                  |
                              [ HistGB Classifier ] -------------------------+
                              Accuracy: 89.11%
                              artifacts/models/lgbm_model.pkl
```

---

## 📊 Feature Definitions

| Feature Name | Type | Description |
| :--- | :--- | :--- |
| `lead_time` | Integer | Days between reservation booking date and arrival date |
| `no_of_special_requests`| Integer | Number of special requests made by customer (e.g. high floor, extra bed) |
| `avg_price_per_room` | Float | Average daily rate per room |
| `arrival_month` | Integer | Month of arrival (1-12) |
| `arrival_date` | Integer | Day of arrival (1-31) |
| `market_segment_type` | Categorical | Booking source (0: Aviation, 1: Complimentary, 2: Corporate, 3: Offline, 4: Online) |
| `no_of_week_nights` | Integer | Total week nights booked (Mon-Fri) |
| `no_of_weekend_nights` | Integer | Total weekend nights booked (Sat-Sun) |
| `type_of_meal_plan` | Categorical | Meal package (0: Plan 1, 1: Plan 2, 2: Plan 3, 3: Not Selected) |
| `room_type_reserved` | Categorical | Room tier (0 to 6) |

---

## 📜 License
This project is open-source and licensed under the [MIT License](LICENSE).
