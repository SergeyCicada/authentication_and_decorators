"""Реализация декоратора для полноценной валидации токена"""

import jwt
from flask import request, abort, Flask
from flask_restx import Api, Resource

algo = 'HS256'
secret = 's3cR$eT'


def auth_required(func):
    def wrapper(*argc, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']  # извлекаем из заголовков всю информацию
        # Bearer weqweqwe0219wqe.qweoqiwrqirq.lalkjdaskl
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            print("JWT decode Exception", e)
            abort(401)
        return func(*argc, **kwargs)

    return wrapper


app = Flask(__name__)
api = Api(app)
book_ns = api.namespace('')


@book_ns.route('/books')
class BookView(Resource):
    def get(self):
        return [], 200

    @auth_required
    def post(self):
        return "", 201


if __name__ == "__main__":
    app.run()