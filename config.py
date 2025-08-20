# config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"