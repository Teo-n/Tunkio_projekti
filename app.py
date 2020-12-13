from flask import Flask
from flask_restful import Api
from extensions import db, jwt
from resources.user import UserListResource, UserResource
from resources.token import TokenResource

from resources.client import ClientListResource, ClientResource, ClientPublishResource
from resources.reservation import ReservationListResource, ReservationResource, ReservationPublishResource
from resources.workspace import WorkspaceListResource, WorkspaceResource, WorkspacePublishResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ClientListResource, '/clients')
api.add_resource(ClientResource, '/clients/<int:client_id>')
api.add_resource(ClientPublishResource, '/clients/<int:client_id>/publish')

api.add_resource(ReservationListResource, '/reservations')
api.add_resource(ReservationResource, '/reservations/<int:reservation_id>')
api.add_resource(ReservationPublishResource, '/reservations/<int:reservation_id>/publish')

api.add_resource(WorkspaceListResource, '/workspaces')
api.add_resource(WorkspaceResource, '/workspaces/<int:workspace_id>')
api.add_resource(WorkspacePublishResource, '/workspaces/<int:workspace_id>/publish')


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app,db)
    jwt.init_app(app)

def register_resources(app):
    api = Api(app)

    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:username>')

    api.add_resource(TokenResource, '/token')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
