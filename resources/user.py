from flask import request
from flask_restful import Resource
from http import HTTPStatus

from utils import hash_password
from models import client


class userListResource(Resource):
    def post(self):
        json_data = request.get_json()

        username = json_data.get('username')
        email = json_data.get('email')

        if client.get_by_username(username):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST

        if client.get_by_email(email):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST




        user = User(
            username=username,
            email=email,
            password=password
        )

        user.save()

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'password': user.password
        }
        return data, HTTPStatus.CREATED



