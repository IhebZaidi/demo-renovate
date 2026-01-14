from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from app.database import engine, get_db, Base
from app.routers import users, items
from app import models

# Créer les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestion",
    description="Application FastAPI de démonstration pour Renovate",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])


@app.get("/")
async def root():
    """Point d'entrée principal de l'API"""
    return {
        "message": "Bienvenue sur l'API de Gestion",
        "version": "1.0.0",
        "documentation": "/docs",
        "dependencies": {
            "fastapi": "0.95.0",
            "sqlalchemy": "1.4.46",
            "pydantic": "1.10.5"
        }
    }


@app.get("/health")
async def health_check():
    """Vérification de l'état de l'application"""
    return {
        "status": "healthy",
        "database": "connected"
    }


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
