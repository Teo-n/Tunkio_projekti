from flask import request
from flask_restful import Resource
from http import HTTPStatus
from marshmallow import Schema, fields
from utils import hash_password

from models.client import Client, client_list


class ClientListResource(Resource):

    def get(self):

        data = []

        for client in client_list:
            if client.is_publish is True:
                data.append(client.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        client = Client(name=data['name'],
                        email=data['email'])

        client_list.append(client)

        return client.data, HTTPStatus.CREATED


class ClientResource(Resource):

    def get(self, client_id):
        client = next((client for client in client_list if client.id == client_id and client.is_publish == True), None)

        if client is None:
            return {'message': 'client not found'}, HTTPStatus.NOT_FOUND

        return client.data, HTTPStatus.OK

    def put(self, client_id):
        data = request.get_json()

        client = next((client for client in client_list if client.id == client_id), None)

        if client is None:
            return {'message': 'client not found'}, HTTPStatus.NOT_FOUND

        client.name = data['name']
        client.description = data['description']
        client.num_of_servings = data['num_of_servings']
        client.cook_time = data['cook_time']
        client.directions = data['directions']

        return client.data, HTTPStatus.OK

    def delete(self, client_id):
        client = next((client for client in client_list if client.id == client_id), None)

        if client is None:
            return {'message': 'client not found'}, HTTPStatus.NOT_FOUND

        client_list.remove(client)

        return {}, HTTPStatus.NO_CONTENT


class ClientPublishResource(Resource):

    def put(self, client_id):
        client = next((client for client in client_list if client.id == client_id), None)

        if client is None:
            return {'message': 'client not found'}, HTTPStatus.NOT_FOUND

        client.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, client_id):
        client = next((client for client in client_list if client.id == client_id), None)

        if client is None:
            return {'message': 'client not found'}, HTTPStatus.NOT_FOUND

        client.is_publish = False

        return {}, HTTPStatus.NO_CONTENT

class SimpleSchema(Schema):

    id = fields.Int(
    username = fields.String(required=True),
    password = fields.Method(required=True, deserialize='load_password'))
    def load_password(self, value):
        return hash_password(value)


