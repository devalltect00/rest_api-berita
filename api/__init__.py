from flask import Flask, render_template
from flask_restx import Api
from .auth.views import auth_namespace
from .news.views import news_namespace
from .config.config import config_dict
from werkzeug.exceptions import NotFound, MethodNotAllowed
from flask_cors import CORS
import os

def create_app(config=config_dict['development']):
    app=Flask(__name__,
              template_folder=os.path.abspath("api/templates"),
              static_folder=os.path.abspath("api/static"))

    @app.route('/')
    def welcome():
        return render_template('welcome.html')

    #### setup CORS

    CORS(app)

    ####

    app.config.from_object(config)

    api = Api(app,
              version="1.1",
              title="Berita API",
              description="Sebuah API untuk mendapatkan berita secara otomatis",
              doc="/docs")
    
    

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