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

```
┌─────────────────────────────────────────┐
│        Data Ingestion & Validation      │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│      Feature Engineering & Processing   │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│         Model Training & Evaluation     │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│           REST API & Deployment         │
└─────────────────────────────────────────┘
```

## Installation

### Prerequisites
- Python 3.8+
- pip or conda
- Docker (optional, for containerization)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
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

### Parameters (params.yaml)

Define model parameters, data paths, and pipeline settings:

```yaml
data_ingestion:
  source_URL: ...
  local_data_file: data/raw.csv

model_training:
  algorithm: RandomForest
  hyperparameters:
    n_estimators: 100
    max_depth: 10
```

### Configuration (config.yaml)

Application-level configuration:

```yaml
artifacts_root: artifacts/
log_level: INFO
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

**Author:** [Kishor Kumar Paroi]  
**Last Updated:** April 2026
```
