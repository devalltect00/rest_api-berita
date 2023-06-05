from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY','secret')

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class TestConfig(Config):
    pass

class ProdConfig(Config):
    DEBUG=config('DEBUG',cast=bool)
    SQLALCHEMY_TRACK_MODIFICATIONS=False

config_dict={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}