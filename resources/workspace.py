from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.workspace import Workspace, workspace_list


class WorkspaceListResource(Resource):

    def get(self):

        data = []

        for workspace in workspace_list:
            if workspace.is_publish is True:
                data.append(workspace.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        workspace = Workspace(building=data['building'],
                              room_type=data['room_type'],
                              floor=data['floor'],
                              room_number=data['room_number'])

        workspace_list.append(workspace)

        return workspace.data, HTTPStatus.CREATED


class WorkspaceResource(Resource):

    def get(self, workspace_id):
        workspace = next((workspace for workspace in workspace_list if workspace.id == workspace_id and workspace.is_publish == True), None)

        if workspace is None:
            return {'message': 'workspace not found'}, HTTPStatus.NOT_FOUND

        return workspace.data, HTTPStatus.OK

    def put(self, workspace_id):
        data = request.get_json()

        workspace = next((workspace for workspace in workspace_list if workspace.id == workspace_id), None)

        if workspace is None:
            return {'message': 'workspace not found'}, HTTPStatus.NOT_FOUND

        workspace.building = data['building']
        workspace.room_type = data['room_type']
        workspace.floor = data['floor']
        workspace.room_number = data['room_number']

        return workspace.data, HTTPStatus.OK


class WorkspacePublishResource(Resource):

    def put(self, workspace_id):
        workspace = next((workspace for workspace in workspace_list if workspace.id == workspace_id), None)

        if workspace is None:
            return {'message': 'workspace not found'}, HTTPStatus.NOT_FOUND

        workspace.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, workspace_id):
        workspace = next((workspace for workspace in workspace_list if workspace.id == workspace_id), None)

        if workspace is None:
            return {'message': 'workspace not found'}, HTTPStatus.NOT_FOUND

        workspace.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
