import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgresqlFord@localhost:5432/flask_vercel'
    SQLALCHEMY_TRACK_MODIFICATIONS = False