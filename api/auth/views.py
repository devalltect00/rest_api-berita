from flask_restx import Namespace,Resource,fields


auth_namespace=Namespace('Otentikasi',description="Sebuah namespace untuk otentikasi")


@auth_namespace.route('/')
class HomeAuth(Resource):
    def get(self):
        return {"message": "Hello"}