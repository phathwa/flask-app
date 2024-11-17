import os

import urllib.parse

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")

    host = "aws-0-eu-central-1.pooler.supabase.com"
    db = "postgres"
    port = 6543
    user = "postgres.xfmjpidwlslhhxiekkpx"
    password = urllib.parse.quote("sS&Phtmer@010")
    DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}/{db}"
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Additional production configurations
