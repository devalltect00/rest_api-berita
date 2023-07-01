from flask_restx import (Resource,
                         Namespace,
                         fields)
from flask_jwt_extended import (jwt_required,
                                get_jwt_identity)
from http import HTTPStatus
from ..models.news import New
from ..models.users import User
from ..utils.db import db
from .newsScrapping import *
from datetime import datetime
from werkzeug.exceptions import Conflict

news_namespace=Namespace('Berita',description="Sebuah Namespace untuk Berita")

news_model=news_namespace.model(
    'News Overview (for input)',{
        'id':fields.Integer(description="id berita"),
        'title':fields.String(required=True, description="judul berita"),
        'synopsis':fields.String(required=True, description="sinopsis berita"),
        'pictureLink':fields.String(required=True, description="tautan gambar berita"),
        'contentLink':fields.String(required=True, description="tautan kontent berita"),
    }
)

news_detail_model=news_namespace.model(
    'News Detail',{
        'id':fields.Integer(description="id berita"),
        'title':fields.String(required=True, description="judul berita"),
        'synopsis':fields.String(required=True, description="sinopsis berita"),
        'pictureLink':fields.String(required=True, description="tautan gambar berita"),
        'contentLink':fields.String(required=True, description="tautan gambar berita"),
        'sourceNews':fields.String(required=False, description="sumber berita"),
        'date':fields.DateTime(required=False, description="tautan gambar berita"),
        'channelName':fields.String(required=False, description="tautan gambar berita"),
        'videoLink':fields.String(required=False, description="tautan gambar berita"),
    }
)

##### Dapatkan sumber berita (external)
@news_namespace.route('/berita/external/<string:newsSource_id>')
class NewsExternalSearch(Resource):
    @news_namespace.doc(
        description="""
Mendapatkan data dari website sumber berita yang tersedia

Cari Sumber berita

Sumber berita yang tersedia:
- "cnn-indonesia",
- "merdeka",
- "suara",
- "detik",
- "kompas",
- "pikiran-rakyat",
- "okezone",

Sumber berita yang tersedia dengan tag:
- "detik-tag-hari_besar"
            """,
        params={
            "newsSource_id":"Sumber berita yang tersedia"
        }
    )
    def get(self,newsSource_id):

        """
            Kumpulan berita berdasarkan sumber berita external
        """


        if "tag" in newsSource_id:
            data = NewsChannel(availableNewsByTag[newsSource_id])
        else:
            data = NewsChannel(availableNews[newsSource_id])
        
        content = data.getContent()

        return {"content" : content}, HTTPStatus.OK

##### Dapatkan kumpulan berita berdasarkan sumber berita (external)
@news_namespace.route('/berita/external/sumber-berita')
class NewsExternalSearchSource(Resource):
    @news_namespace.doc(
        description="Mendapatkan kumpulan sumber berita external yang tersedia"
    )
    def get(self):

        """
            Kumpulan sumber berita external
        """

        sourceNews = SourceNews()
        availableNewsSource = sourceNews.getAvailableNewsSource()
        availableNewsSourceByTag = sourceNews.getAvailableNewsSourceByTag()

        return {"Available News Sources" : availableNewsSource, "Available News Sources By Tag" : availableNewsSourceByTag}, HTTPStatus.OK

##### Mengelola berita (external)
@news_namespace.route('/berita/internal')
class NewsInternal(Resource):

    @news_namespace.marshal_with(news_detail_model)
    @news_namespace.doc(
        description="Mendapatkan semua kumpulan berita internal"
    )
    @jwt_required()
    def get(self):
        """
            kumpulan berita internal
        """

        news = New.query.all()

        return news, HTTPStatus.OK
    
    @news_namespace.expect(news_model)
    @news_namespace.marshal_with(news_detail_model)
    @news_namespace.doc(
        description="Menyimpan berita internal"
    )
    @jwt_required()
    def post(self):
        """
            Simpan
        """

        try:
            data = news_namespace.payload

            new_news = New(
                title=data["title"],
                synopsis=data["synopsis"],
                pictureLink=data["pictureLink"],
                contentLink=data["contentLink"],
                sourceNews="internal"
            )

            new_news.save()

            return new_news, HTTPStatus.CREATED
        
        except Exception as e:
            # raise Conflict(f"Judul dengan nama {data["title"]} sudah ada")
            title=data["title"]
            raise Conflict(f"Judul dengan nama {title} sudah ada")

##### Mengelola berita berdasarkan id (external)
@news_namespace.route('/berita/internal/<int:news_id>')
class NewsInternalById(Resource):

    @news_namespace.marshal_with(news_detail_model)
    @news_namespace.doc(
        description="Mendapatkan semua kumpulan berita internal berdasarkan id berita"
    )
    @jwt_required()
    def get(self, news_id):
        """
            kumpulan berita internal berdasarkan id
        """

        news = New.get_by_id(news_id)

        return news, HTTPStatus.OK
    
    @news_namespace.expect(news_model)
    @news_namespace.marshal_with(news_detail_model)
    @news_namespace.doc(
        description="Mengubah berita internal"
    )
    @jwt_required()
    def put(self, news_id):
        """
            Ubah
        """

        news = New.get_by_id(news_id)

        data = news_namespace.payload

        news.title=data["title"]
        news.synopsis=data["synopsis"]
        news.pictureLink=data["pictureLink"]
        news.contentLink=data["contentLink"]

        db.session.commit()

        return news, HTTPStatus.OK

    @news_namespace.marshal_with(news_detail_model)
    @news_namespace.doc(
        description="Menghapus berita internal"
    )
    # @jwt_required()
    def delete(self, news_id):
        """
            Hapus
        """

        news = New.get_by_id(news_id)
        news.delete()

        return news, HTTPStatus.NO_CONTENT