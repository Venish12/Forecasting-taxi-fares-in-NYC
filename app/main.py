from fastapi import FastAPI
from app.api import router

app = FastAPI(title="NYC Taxi Fare API", version="1.0")
app.include_router(router)
