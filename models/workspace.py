workspace_list = []


def get_last_id():
    if workspace_list:
        last_workspace = workspace_list[-1]
    else:
        return 1
    return last_workspace.id + 1


class Workspace:

    def __init__(self, building, roomType, floor, roomNumber):
        self.id = get_last_id()
        self.building = building
        self.roomType = roomType
        self.floor = floor
        self.roomNumber = roomNumber

        self.is_publish = False

    @property
    def data(self):
        return {
            'id': self.id,
            'building': self.building,
            'roomType': self.roomType,
            'floor': self.floor,
            'roomNumber': self.roomNumber
        }
