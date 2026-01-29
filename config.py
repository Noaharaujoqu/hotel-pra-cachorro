import os

class Config:
    
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'hotelcachorro')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'noah123')
    DB_PORT = os.getenv('DB_PORT', '5432')
    

    SECRET_KEY = os.getenv('SECRET_KEY', 'hotelcachorro')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'hotelcachorro')