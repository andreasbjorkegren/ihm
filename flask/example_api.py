from flask import Flask, request
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)


users = {}

def abort_if_user_id_dont_exist(user_id):
    if user_id not in users:
        abort(404, message="user_id doesn't exist")

def abort_if_user_id_exist(user_id):
    if user_id in users:
        abort(409, message="user_id already exists")

class User(Resource):
    def get(self, user_id):
        abort_if_user_id_dont_exist(user_id)
        return users[user_id]

    def post(self, user_id):
        json_data = request.get_json(force=True)
        print(json_data)
        users[user_id] = json_data
        return  users[user_id], 201

    def delete(self, user_id):
        abort_if_user_id_dont_exist(user_id)
        del users[user_id]
        return '', 204

api.add_resource(User, "/users/<int:user_id>")

if __name__ == '__main__':
    app.run(debug=True)