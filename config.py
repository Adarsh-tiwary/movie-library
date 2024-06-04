# config.py
import os

class Config:
    SECRET_KEY = os.getenv('JWT_SECRET', 'your_jwt_secret')
    MONGO_URI = os.getenv('MONGO_URI', 'your_mongo_uri')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


