workspace_list = []


def get_last_id():
    if workspace_list:
        last_workspace = workspace_list[-1]
    else:
        return 1
    return last_workspace.id + 1


class Workspace:

    def __init__(self, building, room_type, floor, room_number):
        self.id = get_last_id()
        self.building = building
        self.room_type = room_type
        self.floor = floor
        self.room_number = room_number

        self.is_publish = False

    @property
    def data(self):
        return {
            'id': self.id,
            'building': self.building,
            'room_type': self.room_type,
            'floor': self.floor,
            'roomNumber': self.room_number
        }
