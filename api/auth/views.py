from flask_restx import Namespace,Resource,fields
from flask import request
from ..models.users import User
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from http import HTTPStatus
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                get_jwt_identity)
from werkzeug.exceptions import (Conflict,
                                 BadRequest)

auth_namespace=Namespace('Otentikasi',description="Sebuah namespace untuk otentikasi")

signup_model = auth_namespace.model(
    'SignUp',{
        'id':fields.Integer(),
        'username':fields.String(required=True, description="sebuah username"),
        'email':fields.String(required=True, description="Sebuah email"),
        'password':fields.String(required=True, description="Sebuah password"),
    }
)

user_model = auth_namespace.model(
    'User',{
        'id':fields.Integer(),
        'username':fields.String(required=True, description="sebuah username"),
        'email':fields.String(required=True, description="Sebuah email"),
        'password_hash':fields.String(required=True, description="Sebuah password"),
        'is_admin':fields.Boolean(description="Menunjukkan apakah user adalah admin")
    }
)

login_model = auth_namespace.model(
    'Login',{
        'email':fields.String(required=True,description="Email"),
        'password':fields.String(required=True,description="Password")
    }
)

def createAdmin():
    new_user = User(
        username="admin",
        email="admin@gmail.com",
        password_hash=generate_password_hash("123"),
        is_admin=True
    )

    new_user.save()

    return new_user

@auth_namespace.route('/')
class HomeAuth(Resource):
    def get(self):
        return {"message": "Hello"}
    
@auth_namespace.route('/signup')
class Signup(Resource):

    # for inputing data POST request
    # input format
    @auth_namespace.expect(signup_model)
    # for getting response after POST, what data is returned
    # response format
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """
            Buat sebuah akun user baru
        """

        try:
            data = request.get_json()

            # new_user = User(
            #     username=data.get('username'),
            #     email=data.get('email'),
            #     password_hash=generate_password_hash(data.get('password')),
            #     is_admin=data.get('is_admin')
            # )

            new_user = User(
                username=data.get('username'),
                email=data.get('email'),
                password_hash=generate_password_hash(data.get('password'))
            )

            # news.is_admin = True
            new_user.is_admin = True

            new_user.save()

            return new_user, HTTPStatus.CREATED
        
        except Exception as e:
            # handling error
            # raise Conflict(f"User with email {data.get('email')} exists")
            raise Conflict(f"User dengan email {data.get('email')} sudah ada")

@auth_namespace.route('/login')
class Login(Resource):

    @auth_namespace.expect(login_model)
    def post(self):
        """
            Menghasilkan token JWT (login)
            Generate a JWT
        """

        data=request.get_json()

        # email=data('email')
        email=data.get('email')
        user=User.query.filter_by(email=email).first()
        password=data.get('password')

        if user is not None and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity=user.username)
            refresh_token = create_refresh_token(identity=user.username)

            response = {
                'access_token' : access_token,
                'refresh_token' : refresh_token
            }

            return response, HTTPStatus.OK
        
        raise BadRequest("Username atau password tidak valid")
    
@auth_namespace.route('/refresh')
class Refresh(Resource):

    @jwt_required(refresh=True)
    def post(self):
        """
            Menghasilkan token JWT (refresh)
            generate refresh token
        """

        username = get_jwt_identity()

        access_token = create_access_token(identity=username)

        return {'access_token' : access_token}, HTTPStatus.OK