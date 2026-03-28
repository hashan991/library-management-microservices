from fastapi import FastAPI
from app.database import Base, engine
from app.routes.reservation import router as reservation_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Reservation Service",
    description="Microservice for managing library reservations",
    version="1.0.0"
)

app.include_router(reservation_router)


@app.get("/")
def root():
    return {"message": "Reservation Service is running successfully"}