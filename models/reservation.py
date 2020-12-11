reservation_list = []


def get_last_id():
    if reservation_list:
        last_reservation = reservation_list[-1]
    else:
        return 1
    return last_reservation.id + 1


class Reservation:

    def __init__(self, date, time, client):
        self.id = get_last_id()
        self.date = date
        self.time = time
        self.client = client

        self.is_publish = False

    @property
    def data(self):
        return {
            'id': self.id,
            'date': self.date,
            'time': self.time,
            'client': self.client
        }
