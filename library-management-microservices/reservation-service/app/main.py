from fastapi import FastAPI
from app.database import engine, Base
from app.routes.reservation import router as reservation_router
import app.models

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Reservation Service API",
    description="Microservice for managing library reservations",
    version="1.0.0"
)

# Include reservation routes
app.include_router(reservation_router, prefix="/reservations", tags=["Reservations"])


@app.get("/")
def root():
    return {"message": "Reservation Service is running successfully"}