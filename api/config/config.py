import os
from decouple import config
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv('.env.development.local')

# uri = os.environ['POSTGRES_URL']
# if uri.startswith("postgres://"):
    # uri = uri.replace("postgres://", "postgresql://", 1)

uri = None

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=config('SECRET_KEY','secret')
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_SECRET_KEY=config('JWT_SECRET_KEY')

class DevConfig(Config):
    # DEBUG=True
    DEBUG=config('DEBUG',cast=bool)
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIR, 'db.sqlite3')

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # (keep database) in memory_(??)
    SQLALCHEMY_DATABASE_URI = "sqlite://"

class ProdConfig(Config):
    DEBUG=config('DEBUG',cast=bool)
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI=uri

config_dict={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}