from fastapi import FastAPI
from app.database import engine, Base
from app.routes.borrowing import router as borrowing_router
import app.models

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Borrowing Service API",
    description="Microservice for managing library borrowings",
    version="1.0.0"
)

# Include borrowing routes
app.include_router(borrowing_router, prefix="/borrowings", tags=["Borrowings"])


@app.get("/")
def root():
    return {"message": "Borrowing Service is running successfully"}