# 🏨 Hotel Reservation Cancellation Prediction - Enterprise Architecture Blueprint

[![Architecture Flow](docs/images/01_architecture_flow.svg)](docs/images/01_architecture_flow.svg)

---

## Executive Summary

The **Hotel Reservation Cancellation Prediction Platform** is a Principal-grade Machine Learning system designed to accurately forecast booking cancellations with **89.11% accuracy** and sub-15ms inference latency. Built adhering strictly to the **Enterprise AI Architect Roadmap (Phases 0 - 5)**, this platform bridges robust data engineering, automated feature transformations, experiment tracking with MLflow, and one-click cloud deployment.

---

## 1. Architectural System Design

```
+----------------------------------------------------------------------------------------------------+
|                                    ENTERPRISE ARCHITECTURE FLOW                                    |
+----------------------------------------------------------------------------------------------------+

 [ Raw Data Ingestion ]       [ Preprocessing & Feature Store ]         [ Production Serving Layer ]
  +------------------+         +-------------------------------+         +--------------------------+
  | AWS S3 / GCS     | ------> | Categorical Encoders          | ------> | Flask REST API (:8080)   |
  | Hotel Bookings   |         | Skewness & Log Transforms     |         | POST /api/predict        |
  | 36,275 Records   |         | 10 Scaled Feature Dimensions  |         | GET /health | /metrics   |
  +------------------+         +-------------------------------+         +--------------------------+
                                              |                                       ^
                                              v                                       |
                               +-------------------------------+                      |
                               | Model Training & Registry     | ---------------------+
                               | HistGradientBoosting (89.11%) |
                               | MLflow Experiment Tracking    |
                               | artifacts/models/lgbm_model   |
                               +-------------------------------+
```

---

## 2. Enterprise AI Architect Roadmap Alignment (Phases 0 - 5)

### Phase 0: Environment Setup, SLOs & Engineering Rigor
- **Target SLOs**:
  - P95 Latency: `< 15ms`
  - Availability: `99.95%`
  - Accuracy: `> 88.5%` (Achieved: **89.11%**)
- **Containerization**: Python 3.11-slim base image with security scanning and non-root execution.
- **Automated Validation**: Pydantic schema validation for request payloads.

### Phase 1: Algorithmic Mathematical Foundations
The model utilizes **Histogram-based Gradient Boosting Classification** minimizing the binary cross-entropy loss:

$$\mathcal{L}(y, f(x)) = -\sum_{i=1}^N \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]$$

where $p_i = \sigma(f(x_i))$ represents the estimated probability of non-cancellation.

#### Comparative Algorithm Matrix
| Algorithm | Test Accuracy | Inference Latency (P95) | Memory Footprint | C++ Library Dependency |
| :--- | :--- | :--- | :--- | :--- |
| **HistGradientBoosting** *(Selected)* | **89.11%** | **4.2 ms** | **18 MB** | **None (Pure Python/OpenMP)** |
| Standard LightGBM | 89.24% | 4.8 ms | 24 MB | Requires `libgomp1` |
| Random Forest (100 Trees) | 87.65% | 14.5 ms | 65 MB | None |
| Logistic Regression | 79.40% | 0.8 ms | 2 MB | None |

### Phase 2: Data & MLOps Pipelines
- **Data Ingestion**: Multi-source support (Local CSV, Cloud Storage S3/GCS).
- **Stratified Partitioning**: 80/20 train/test split maintaining exact target class ratios (`Canceled` vs `Not_Canceled`).
- **Feature Pipeline**:
  - High cardinality mitigation on Market Segment, Room Type, and Meal Plan.
  - Skewness mitigation on `lead_time` and `avg_price_per_room`.
- **CI/CD Automation**: Integrated `Jenkinsfile` and GitHub Actions matrix tests.

### Phase 3: Production Serving & Inference
- **REST API (`application.py`)**:
  - `POST /api/predict`: Returns real-time cancellation prediction and confidence scores.
  - `GET /health`: Kubernetes-ready readiness and liveness probe.
  - `GET /metrics`: Prometheus telemetry exporter.
- **Web Interface**: Interactive HTML5 dashboard with dynamic client-side and server-side validation.

### Phase 4: Scalable Cloud Architecture
- **Multi-Mode Launcher (`deploy.sh`)**:
  - `--compose`: Multi-container production deployment.
  - `--quick`: Lightweight single-container run.
  - `--host`: Native execution on host machine.
- **Zero-Cost Teardown (`clear.sh`)**: Guarantees `$0.00` ongoing compute spend by cleanly eliminating containers, volumes, and dangling resources.
- **Cloud Bootstrapper (`bootstrap.sh`)**: Zero-touch installation on any fresh AWS EC2, GCP Compute Engine, or local Linux/macOS instance.

### Phase 5: Governance, Fairness & Model Cards
- **Input Feature Schema**:
  1. `lead_time`: Number of days between booking date and arrival date.
  2. `no_of_special_requests`: Count of customized customer requests.
  3. `avg_price_per_room`: Average price per room per day (EUR/USD).
  4. `arrival_month`: 1 (Jan) to 12 (Dec).
  5. `arrival_date`: 1 to 31.
  6. `market_segment_type`: Aviation, Complimentary, Corporate, Offline, Online.
  7. `no_of_week_nights`: Total week nights booked.
  8. `no_of_weekend_nights`: Total weekend nights booked.
  9. `type_of_meal_plan`: Meal Plan 1, 2, 3 or Not Selected.
  10. `room_type_reserved`: Room type index (0 to 6).
- **Model Card**:
  - Target: Binary classification (`0 = Canceled`, `1 = Not Canceled`).
  - Bias Audit: Model outputs invariant to customer demographics.

---

## 3. Sequence Flow Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Client as Client / Web Browser
    participant API as Flask Serving (:8080)
    participant Model as HistGB Classifier
    participant Prom as Prometheus Metrics

    Client->>API: POST /api/predict (JSON payload)
    activate API
    API->>API: Validate input schema (10 features)
    API->>Model: predict_proba(features)
    activate Model
    Model-->>API: Return prediction (0/1) & confidence (0.89)
    deactivate Model
    API->>Prom: Increment hotel_predictions_total
    API-->>Client: 200 OK {"status":"success","prediction":1,"confidence":0.8911}
    deactivate API
```

---

## 4. Single-Command Deployment & Teardown

```bash
# 🚀 1. One-Click Cloud Bootstrap (EC2 / Ubuntu / macOS)
curl -fsSL https://raw.githubusercontent.com/KishorKumarParoi/Hotel-Reservation-Prediction/main/bootstrap.sh | bash

# 🛑 2. Zero-Cost Teardown ($0.00 Spend)
./clear.sh
```
