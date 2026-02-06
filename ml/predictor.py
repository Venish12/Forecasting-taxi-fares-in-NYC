from pathlib import Path
import joblib
import pandas as pd

from ml.features import make_features, FEATURE_ORDER


class TaxiFarePredictor:
    def __init__(self, model_path: Path):
        self.model_path = model_path
        self.pipeline = None

    def load(self):
        if self.pipeline is None:
            bundle = joblib.load(self.model_path)
            self.pipeline = bundle["pipeline"]

    def predict_one(self, payload: dict) -> float:
        self.load()

        raw_df = pd.DataFrame([payload])
        X = make_features(raw_df)
        X = X[FEATURE_ORDER]

        return float(
            self.pipeline.predict(X, validate_features=False)[0]
        )
