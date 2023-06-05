from flask import Flask
from flask_restx import Api
from .auth.views import auth_namespace
from .news.views import news_namespace
from .config.config import config_dict

def create_app(config=config_dict['development']):
    app=Flask(__name__)

    app.config.from_object(config)

    api = Api(app)

    # api.add_namespace(news_namespace,port='/')
    api.add_namespace(news_namespace,path='/api')
    api.add_namespace(auth_namespace,path='/auth')


    return app