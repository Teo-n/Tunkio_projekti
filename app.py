from flask import Flask, jsonify, request
from http import HTTPStatus

# creating app
app = Flask(__name__)

# creating table
clients = {
    'id',
    'name',
    'email'
}

# creating table
workspaces = {
    'id',
    'building',
    'roomType',
    'floor',
    'roomNumber'
}

# creating table
reservations = {
    'id',
    'date',
    'time',
    'client'
}


# CLIENTS TABLE
# GET response returns all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    return jsonify({'data': clients})


# GET response returns one client by id
@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = next((client for client in clients if client['id'] == client_id), None)

    if client:
        return jsonify(client)
# if client is not found, error message is shown
    return jsonify({'message': 'Cannot find client'}), HTTPStatus.NOT_FOUND


# POST response returns name and email values
@app.route('/clients', methods=['POST'])
def create_client():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')

    client = {
        'id': + 1,
        'name': name,
        'email': email
    }

    clients.append(client)
# return created client (has JSON format and HTTP status)
    return jsonify(client), HTTPStatus.CREATED


# PUT response edits a client by id
@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = next((client for client in clients if client['id'] == client_id), None)

    if not client:
        return jsonify({'message': 'Cannot find client'}), HTTPStatus.NOT_FOUND

# If the client is found, the update function will be performed
    data = request.get_json()

    client.update(
        {
            'name': data.get('name'),
            'email': data.get('email')
        }
    )

    return jsonify(client)


if __name__ == '__main__':
    app.run()