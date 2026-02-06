from fastapi import APIRouter, HTTPException
from pathlib import Path

from app.schemas import TaxiFareRequest, TaxiFareResponse
from ml.predictor import TaxiFarePredictor

router = APIRouter(prefix="/api/v1")

MODEL_PATH = Path(__file__).resolve().parent.parent / "ml" / "artifacts" / "taxi_fare_pipeline_bundle.pkl"
predictor = TaxiFarePredictor(MODEL_PATH)

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/predict", response_model=TaxiFareResponse)
def predict(req: TaxiFareRequest):
    try:
        fare = predictor.predict_one(req.model_dump())
        return TaxiFareResponse(fare_amount=fare)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Model artifact not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
