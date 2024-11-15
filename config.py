import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgres://postgres.gnrhccivkfbfxmwxlxcj:Dk6vCJdNYuinpouP@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres?sslmode=require&supa=base-pooler.x')
    SQLALCHEMY_TRACK_MODIFICATIONS = False