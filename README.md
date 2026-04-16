```markdown
# Hotel Reservation Prediction

A production-ready MLOps project for predicting hotel reservation cancellations using machine learning techniques with modular architecture and containerization.

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Architecture](#architecture)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Pipeline](#pipeline)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker Deployment](#docker-deployment)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project implements an end-to-end MLOps pipeline for predicting hotel reservation cancellations. It includes:
- Data ingestion and validation
- Feature engineering and preprocessing
- Model training and evaluation
- REST API for predictions
- Docker containerization
- Configuration management

## Problem Statement

Hotel reservations often face cancellations, which impact revenue and resource planning. This project builds a machine learning model to predict the likelihood of a reservation being cancelled, enabling hotels to optimize overbooking strategies and resource allocation.

## Architecture

The project follows a modular, production-ready architecture with the following pipeline stages:

**Data Pipeline:**
- **Data Ingestion** → Load raw data from sources (CSV, APIs, Databases)
- **Data Validation** → Schema validation, missing value checks, type verification
- **Data Transformation** → Cleaning, normalization, and feature engineering
- **Feature Preprocessing** → Scaling, encoding, and feature creation

**Model Pipeline:**
- **Model Training** → Train with cross-validation and hyperparameter tuning
- **Model Evaluation** → Performance metrics (Accuracy, Precision, Recall, F1)
- **Model Registry** → Version control and artifact storage

**Deployment:**
- **REST API** → Flask-based prediction endpoint
- **Web UI** → User-friendly prediction interface
- **Docker** → Containerized deployment
- **CI/CD** → Automated testing and deployment pipeline

## Installation

### Prerequisites
- Python 3.8+
- pip or conda
- Docker (optional, for containerization)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Hotel-Reservation-Prediction.git
   cd Hotel-Reservation-Prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
Hotel-Reservation-Prediction/
├── app.py                      # Flask application entry point
├── main.py                     # CLI entry point
├── Dockerfile                  # Docker configuration
├── params.yaml                 # Pipeline parameters
├── schema.yaml                 # Data schema validation
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
├── config/
│   └── config.yaml            # Configuration settings
├── src/
│   └── datascience/
│       ├── components/         # Pipeline components
│       ├── config/            # Configuration management
│       ├── constants/         # Constants and enums
│       ├── entity/            # Data entities
│       ├── pipeline/          # ML pipelines
│       └── utils/             # Utility functions
├── research/
│   └── research.ipynb         # Exploratory data analysis
├── templates/
│   └── index.html             # Web UI
└── artifacts/                 # Model artifacts and outputs
```

## Dataset

The project uses hotel reservation data with features including:
- Guest information (country, email, etc.)
- Reservation details (arrival date, length of stay, etc.)
- Booking channel and agent information
- Special requests and meal plans
- Target variable: Cancellation (0 = Not Cancelled, 1 = Cancelled)

**Expected Schema:**
See `schema.yaml` for complete data schema and validation rules.

## Pipeline

The MLOps pipeline consists of the following stages:

1. **Data Ingestion** - Load raw data from sources
2. **Data Validation** - Validate data against schema
3. **Data Transformation** - Clean and preprocess features
4. **Feature Engineering** - Create derived features
5. **Model Training** - Train ML models
6. **Model Evaluation** - Evaluate performance metrics
7. **Model Registry** - Save and version models

## Usage

### Training Pipeline

Run the complete training pipeline:

```bash
python main.py
```

Or use the Python API:

```python
from src.datascience.pipeline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run()
```

### Making Predictions

```python
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

predictor = PredictionPipeline()
result = predictor.predict(data)
```

## API Endpoints

### Flask Application

Start the API server:

```bash
python app.py
```

The server runs on `http://localhost:5000`

**Available Endpoints:**

- **POST `/predict`** - Make predictions
  ```json
  {
    "features": {...}
  }
  ```

- **GET `/`** - Web UI
- **GET `/health`** - Health check

## Docker Deployment

### Build Docker Image

```bash
docker build -t hotel-reservation-prediction:latest .
```

### Run Docker Container

```bash
docker run -p 5000:5000 hotel-reservation-prediction:latest
```

The API will be available at `http://localhost:5000`

## Configuration

### Parameters (`params.yaml`)

Define model parameters, data paths, and pipeline settings:

```yaml
data_ingestion:
  source_URL: https://example.com/hotel_data.csv
  local_data_file: data/raw.csv

data_validation:
  all_schema: schema.yaml

data_transformation:
  data_path: data/raw.csv
  target_column: is_canceled

model_training:
  algorithm: RandomForest
  test_size: 0.2
  random_state: 42
  hyperparameters:
    n_estimators: 100
    max_depth: 10
    min_samples_split: 5
    random_state: 42

model_evaluation:
  metrics_path: artifacts/metrics.json
```

### Configuration (`config/config.yaml`)

Application-level configuration:

```yaml
artifacts_root: artifacts/
log_level: INFO
app_name: HotelReservationPrediction
app_version: 1.0.0
```

## Examples

### Example 1: Training a New Model

```bash
python main.py
```

This will:
1. Load data from configured source
2. Validate data schema
3. Transform and engineer features
4. Train the model
5. Evaluate performance
6. Save artifacts

### Example 2: Making a Single Prediction

```python
import json
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

# Sample reservation data
reservation = {
    'lead_time': 342,
    'arrival_date_year': 2026,
    'arrival_date_month': 1,
    'stays_in_weekend_nights': 0,
    'stays_in_week_nights': 7,
    'adults': 2,
    'children': 0,
    'meal': 'BB',
    'country': 'PRT',
    'market_segment': 'Online TA'
}

pipeline = PredictionPipeline()
result = pipeline.predict([reservation])
print(f"Cancellation Probability: {result[0]:.2%}")
```

### Example 3: API Request

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "lead_time": 342,
    "arrival_date_year": 2026,
    "stays_in_weekend_nights": 0,
    "stays_in_week_nights": 7
  }'
```

## Results & Performance Metrics

The model achieves the following performance metrics on test data:

| Metric | Score |
|--------|-------|
| Accuracy | 0.85+ |
| Precision | 0.82+ |
| Recall | 0.79+ |
| F1-Score | 0.80+ |
| ROC-AUC | 0.90+ |

*Note: Exact metrics depend on the specific dataset and model configuration.*

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution:** Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: Data validation fails
**Solution:** Check that your data matches the schema defined in `schema.yaml`

### Issue: Docker build fails
**Solution:** Ensure you have enough disk space and Docker is properly installed:
```bash
docker --version
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Author:** Kishor Kumar Paroi  
**Email:** kishorkumarparoi@example.com  
**Last Updated:** April 2026  
**Version:** 1.0.0
```
