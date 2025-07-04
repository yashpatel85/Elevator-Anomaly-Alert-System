import os
from sqlalchemy import create_engine, Column, Integer, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine)
Base = declarative_base()

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key = True, index = True)
    timestamp = Column(DateTime, default = datetime.utcnow)
    anomaly_score = Column(Float)
    is_anomaly = Column(Boolean)

    vibration_mean = Column(Float)
    vibration_std = Column(Float)
    vibration_max = Column(Float)
    vibration_min = Column(Float)

    humidity_mean = Column(Float)
    humidity_std = Column(Float)
    humidity_max = Column(Float)
    humidity_min = Column(Float)

    revolution_mean = Column(Float)
    revolution_std = Column(Float)
    revolution_max = Column(Float)
    revolution_min = Column(Float)

Base.metadata.create_all(bind = engine)