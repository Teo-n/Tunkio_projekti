client_list = []


def get_last_id():
    if client_list:
        last_client = client_list[-1]
    else:
        return 1
    return last_client.id + 1


class Client:

    def __init__(self, name, email):
        self.id = get_last_id()
        self.name = name
        self.email = email

        self.is_publish = False

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
