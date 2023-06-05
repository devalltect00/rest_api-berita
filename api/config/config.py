from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY','secret')

class DevConfig(Config):
    DEBUG=config('DEBUG',cast=bool)

class TestConfig(Config):
    pass

class ProdConfig(Config):
    pass

config_dict={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}