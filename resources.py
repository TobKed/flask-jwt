from flask_restful import Resource, reqparse
from models import UserModel


parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        username = data['username']

        if UserModel.find_by_username(username):
            return {'message': f'User {username} already exists'}

        new_user = UserModel(
            username=username,
            password=data['password']
        )
        new_user.save_to_db()
        return {'message': f'User {username} was created'}


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        return data


class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class AllUsers(Resource):
    def post(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}


class SecretResource(Resource):
    def get(self):
        return {'answer': 'secret answer'}
