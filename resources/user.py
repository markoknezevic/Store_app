import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
class UserRegister(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('username',
    type=str,
    required=True,
    help="This field is mandatory")

    parse.add_argument('password',
    type=str,
    required=True,
    help="This field is mandatory")


    def post(self):
        data = UserRegister.parse.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {'message': 'Username taken'}, 400

        user = UserModel(**data)#data["username"],data["password"]
        user.save_to_db()
