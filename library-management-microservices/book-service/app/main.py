import os
from fastapi import FastAPI
from dotenv import load_dotenv
from .database import Base, engine
from .routers import books

load_dotenv()

app_name = os.getenv("APP_NAME", "Book Service")

app = FastAPI(
    title=app_name,
    description="Library Management System - Book Service",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(books.router)

@app.get("/")
def root():
    return {"message": f"{app_name} is running"}

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "book-service"}