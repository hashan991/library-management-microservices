from fastapi import FastAPI
from app.database import engine, Base
from app.routes.members import router as member_router
import app.models

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Member Service API",
    description="Microservice for managing library members",
    version="1.0.0"
)

# Include member routes
app.include_router(member_router, prefix="/members", tags=["Members"])


@app.get("/")
def root():
    return {"message": "Member Service is running successfully"}