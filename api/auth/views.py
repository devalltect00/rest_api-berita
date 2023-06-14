from flask_restx import Namespace,Resource,fields
from flask import request

auth_namespace=Namespace('Otentikasi',description="Sebuah namespace untuk otentikasi")

login_model = auth_namespace.model(
    'Login',{
        'email':fields.String(required=True,description="Email"),
        'password':fields.String(required=True,description="Password")
    }
)

@auth_namespace.route('/')
class HomeAuth(Resource):
    def get(self):
        return {"message": "Hello"}
    
@auth_namespace.route('/signup')
class HomeAuth(Resource):
    def post(self):
        """Belum Diatur"""
        return {"message": "Belum diatur"}
    
@auth_namespace.route('/login')
class HomeAuth(Resource):
    def post(self):
        """
            Generate a JWT
        """
        data=request.get_json()

        return {"message": "Belum diatur"}