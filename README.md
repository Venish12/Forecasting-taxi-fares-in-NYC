# New York Taxi Fare Prediction API

A production-oriented **machine learning inference API** that predicts New York City taxi fares using **FastAPI** and an **XGBoost regression model**.  
The project focuses on **reliable model serving**, consistent feature processing, and clean deployment practices.

---

## Overview

The API estimates taxi fares based on trip-level metadata such as pickup and dropoff locations, pickup time, and passenger count.  
All feature engineering and inference logic is executed through a single pipeline, ensuring consistency between model logic and API behavior.

---

## Machine Learning Approach

- **Model**: XGBoost Regressor  
- **Artifact**: Serialized inference pipeline (`.pkl`)  
- **Inference Strategy**: End-to-end pipeline execution for deterministic predictions  

### Feature Engineering

The model derives structured features from raw inputs, including:

- Datetime decomposition  
  - Year, month, day, weekday, hour
- Haversine distance between pickup and dropoff coordinates
- Distance to major NYC reference points:
  - JFK Airport
  - LaGuardia Airport
  - Newark Airport
  - Metropolitan Museum of Art
  - World Trade Center

These features capture both spatial and temporal trip dynamics while maintaining interpretability.

---

## Project Structure

```text
NEWYORK_TAXI_FARE_API/
├── app/
│   ├── main.py            # FastAPI application entry point
│   ├── api.py             # API routes
│   └── schemas.py         # Request and response models
├── ml/
│   ├── features.py        # Feature engineering logic
│   ├── predictor.py       # Model loading and inference
│   └── artifacts/
│       └── taxi_fare_pipeline_bundle.pkl
├── tests/
│   └── test_predict.py    # API tests
├── notebooks/
│   └── training.ipynb     # Model development notebook
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
└── README.md
```
## API Endpoints

### Predict Taxi Fare

**POST** `/api/v1/predict`

Returns an estimated taxi fare for a single trip.

#### Request Body
```json
{
  "pickup_datetime": "2015-01-27 13:08:24 UTC",
  "pickup_longitude": -73.9851,
  "pickup_latitude": 40.7589,
  "dropoff_longitude": -73.9772,
  "dropoff_latitude": 40.7527,
  "passenger_count": 1
}
```
#### Response
```json
{
  "predicted_fare": 11.42
}
```
## Running the API with Docker

### Requirements
- Docker
- Docker Compose

### Start the Service
```bash
docker compose up --build
```
##### The API will be available at:
```
http://localhost:8000
http://localhost:8000/docs
```
