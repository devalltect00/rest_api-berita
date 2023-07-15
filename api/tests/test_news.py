import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils.db import db
from ..models.news import New
from flask_jwt_extended import create_access_token

class UserTestCase(unittest.TestCase):
    def setUp(self):
        # self.app = create_app(config=config_dict['testing'])
        self.app = create_app(config=config_dict['test'])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.app=None
        self.appctx.pop()
        self.client=None

    def testGetInternalNews(self):
        token = create_access_token(identity="admintest")
        headers={
            "Authorization" : f"Bearer {token}"
        }
        response=self.client.get('/api/berita/internal',headers=headers)
        assert response.status_code == 200
        # assert response.json == []
        assert response.json == {"items" : []}
    
    def testPostInternalNews(self):
        data={
            "title": "berita untuk test",
            "synopsis": "ini adalah berita terbaru untuk test",
            "pictureLink": "https:picturelink test",
            "contentLink": "https:contentlink test"
        }
        token = create_access_token(identity="admintest")
        headers={
            "Authorization" : f"Bearer {token}"
        }
        response=self.client.post('/api/berita/internal',json=data,headers=headers)
        assert response.status_code == 201
        news = New.query.all()
        assert len(news) == 1