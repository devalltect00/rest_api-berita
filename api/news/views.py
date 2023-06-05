from flask_restx import Resource,Namespace,fields
from http import HTTPStatus
from ..models.news import News
# from .newsScrapping import *
from .newsScrapping import *

news_namespace=Namespace('Berita',description="Sebuah Namespace untuk Berita")

# @news_namespace.route('/berita/<int:newsSource_id>')
@news_namespace.route('/berita/<string:newsSource_id>')
class NewsSearch(Resource):
    def get(self,newsSource_id):

        """
            Cari Sumber berita
            Tersedia:
            "cnn-indonesia",
            "merdeka",
            "suara",
            "detik",
            "kompas",
            "pikiran-rakyat",
            "okezone"
        """

        data = NewsChannel(availableNews[newsSource_id])

        return {"content" : data.getContent()}, HTTPStatus.OK
    
@news_namespace.route('/berita/sumber-berita')
class NewsSearch(Resource):
    def get(self):

        """
            Daftar sumber berita yang tersedia
        """

        sourceNews = SourceNews()

        return {"sourceNews" : sourceNews.getAvailableNewsSource()}, HTTPStatus.OK