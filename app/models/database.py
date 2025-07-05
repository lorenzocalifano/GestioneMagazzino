from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path

# Usa un percorso assoluto per il database
BASE_DIR = Path(__file__).resolve().parent.parent
SQLALCHEMY_DATABASE_URL = f"sqlite:///{BASE_DIR}/app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True  # Abilita logging SQL per debug
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()