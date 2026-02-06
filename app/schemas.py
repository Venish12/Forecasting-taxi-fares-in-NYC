from pydantic import BaseModel, Field

class TaxiFareRequest(BaseModel):
    pickup_datetime: str = Field(..., description="Example: 2015-01-27 13:08:24 UTC")

    pickup_longitude: float = Field(..., ge=-75, le=-72)
    dropoff_longitude: float = Field(..., ge=-75, le=-72)
    pickup_latitude: float = Field(..., ge=40, le=42)
    dropoff_latitude: float = Field(..., ge=40, le=42)
    passenger_count: int = Field(..., ge=1, le=6)

class TaxiFareResponse(BaseModel):
    fare_amount: float
