from api import create_app
from api.config.config import config_dict
from flask import Flask, render_template
import os

app = create_app(config=config_dict['production'])
# app = create_app(config=config_dict['development'])

if __name__ == '__main__':
    # @app.route('/')
    # def welcome():
    #     return render_template('welcome.html')

    app.run()