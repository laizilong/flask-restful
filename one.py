from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

USERS = [
    {"name": "张三"},
    {"name": "lisi"},
    {"name": "John"},
    {"name": "六六"},
]

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, location='json', help='name不能为空')  ## 表示这项参数必须传，不传报错，并提示


class UserList(Resource):
    def get(self):
        args = parser.parse_args()  ##这个是通过body中的json进行取值
        name = request.args.get('name')
        print(name)
        if name is None:
            return jsonify(USERS)
        elif args not in USERS:
            return jsonify({"msg": "没有该名字"})
        return jsonify(args)

    def post(self):
        name = request.get_json()
        if name not in USERS:
            USERS.append(name)
        return jsonify(USERS)

    def delete(self):
        global USERS
        args = parser.parse_args()
        name = args.get('name')
        # print(args)
        if name is None:
            USERS = []
            return jsonify(USERS)
        if name is not None:
            USERS.remove(args)
        return jsonify(USERS)

    def put(self):
        args = parser.parse_args()
        newname = args.get('name')
        userid = request.json.get('userid')
        USERS[int(userid)] = {"name": newname}
        return jsonify(USERS)


app = Flask(__name__)
api = Api(app)

api.add_resource(UserList, '/user')
# api.add_resource(User, '/user/<int:userid>')
# api.add_resource(User, )
# api.add_resource(UserId, '/user/<userid>')
# api.add_resource(PostId, '/user/<userid>/<newname>')
# api.add_resource(DeleteId, '/user/<userid>')

app.run(host='0.0.0.0', port=5001, use_reloader=True)
