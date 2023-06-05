from flask import Flask
from flask_restx import Api
from .auth.views import auth_namespace
from .news.views import news_namespace
from .config.config import config_dict
from werkzeug.exceptions import NotFound, MethodNotAllowed
from flask_cors import CORS

def create_app(config=config_dict['development']):
    app=Flask(__name__)

    #### setup CORS

    CORS(app)

    ####

    app.config.from_object(config)

    api = Api(app,
              title="Berita API",
              description="Sebuah API untuk mendapatkan berita secara otomatis")
    
    @api.errorhandler(NotFound)
    def not_found(error):
        return {"error":"Tidak ditemukan"},404
    
    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {"error":"Method Not Allowed"},405

    # api.add_namespace(news_namespace,port='/')
    api.add_namespace(news_namespace,path='/api')
    api.add_namespace(auth_namespace,path='/auth')

    # @app.shell_context_processor
    # def make_shell_context():
    #     return {
    #         'User':
    #     }

    return app