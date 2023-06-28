import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils.db import db
from ..models.users import User
from werkzeug.security import generate_password_hash

class UserTestCase(unittest.TestCase):
    def setUp(self):
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

    def testUserSignup(self):
        data={
            "username": "admintest",
            "email": "admintest@gmail.com",
            "password": "12345"
        }
        response = self.client.post('/auth/signup', json=data)
        # user = User.query.filter_by(email=data["admintest@gmail.com"]).first()
        user = User.query.filter_by(email=data["email"]).first()
        assert user.username == "admintest"
        assert response.status_code == 201
    
    def testUserLogin(self):
        data={
            "email": "admintest@gmail.com",
            "password": "12345"
        }
        response = self.client.post('/auth/login', json=data)
        assert response.status_code == 400