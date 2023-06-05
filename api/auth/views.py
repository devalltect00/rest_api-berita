from flask_restx import Namespace,Resource,fields


auth_namespace=Namespace('Otentikasi',description="Sebuah namespace untuk otentikasi")


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
        """Belum Diatur"""
        return {"message": "Belum diatur"}