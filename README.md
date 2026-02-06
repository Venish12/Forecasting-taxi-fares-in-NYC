# New York Taxi Fare Prediction API

A production-ready machine learning API that predicts New York City taxi fares using FastAPI and an XGBoost regression model.  
This project demonstrates real-world ML engineering practices including robust feature engineering, pipeline-based inference, automated testing, and a clean deployment-oriented architecture.

---

## Overview

The API estimates taxi fares based on trip metadata such as pickup and dropoff locations, pickup time, and passenger count.  
All feature engineering and inference logic is handled consistently through a trained machine learning pipeline to ensure reliable and reproducible predictions.

---

## Machine Learning Approach

- **Model**: XGBoost Regressor
- **Artifact Format**: Serialized pipeline (`.pkl`)
- **Inference Strategy**: Pipeline-based prediction to guarantee training–serving consistency

### Feature Engineering
The model uses engineered features derived from raw inputs:
- Datetime decomposition (year, month, day, weekday, hour)
- Haversine distance between pickup and dropoff points
- Distance from major NYC landmarks:
  - JFK Airport
  - LaGuardia Airport
  - Newark Airport
  - Metropolitan Museum of Art
  - World Trade Center

This approach improves predictive accuracy while maintaining interpretability.

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
│   └── training.ipynb     # Model training notebook
├── requirements.txt
├── pytest.ini
└── README.md

```
---
### Predict Taxi Fare

**POST** `/api/v1/predict`

Predicts the estimated taxi fare for a single trip based on pickup and dropoff details.

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


