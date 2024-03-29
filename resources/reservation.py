from flask import request
from flask_restful import Resource
from http import HTTPStatus
from marshmallow import Schema, fields
from schemas.reservation import ReservationSchema
from extensions import jwt


from models.reservation import Reservation, reservation_list
reservation_schema = ReservationSchema()
reservation_public_schema = ReservationSchema(exclude=('client',))
reservation_list_schema = ReservationSchema(many=True)


# Get and Post methods are defined
class ReservationListResource(Resource):

    def get(self):

        reservation = Reservation.get_all_published()

        return reservation_list_schema.dump(reservation).data, HTTPStatus.OK

    @jwt_required
    def post(self):

        json_data = request.get_json()
        current_reservation = get_jwt_identity()
        data, errors = reservation_schema.load(data=json_data)

        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        if current_reservation.get_by_id(data.get('id')):
            return {'message': 'id already used'}, HTTPStatus.BAD_REQUEST

        if current_reservation.get_by_date(data.get('date')):
            return {'message': 'date not selectable'}, HTTPStatus.BAD_REQUEST

        if current_reservation.get_by_time(data.get('time')):
            return {'message': 'time not selectable'}, HTTPStatus.BAD_REQUEST

        if current_reservation.get_by_number_of_Reservations(data.get('number_of_Reservations')):
            return {'message': 'Already booked'}, HTTPStatus.BAD_REQUEST

        reservation = current_reservation(**data)
        reservation.id = current_reservation
        reservation.save()

        return reservation_schema.dump(reservation).data, HTTPStatus.CREATED


# Get and Put methods are defined
class ReservationResource(Resource):

    @jwt_optional
    def get(self, reservation_id):

        reservation = Reservation.get_by_id(id=id)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        current_reservation = get_jwt_identity()

        if current_reservation == reservation.id:
            data = reservation_schema.dump(reservation).data

        else:
            data = reservation_public_schema.sump(reservation).data

            return data, HTTPStatus.OK

    def put(self, reservation_id):
        data = request.get_json()

        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        reservation.date = data['date']
        reservation.time = data['time']
        reservation.client = data['client']
        reservation.number_of_Reservations = data['Number of reservations']

        return reservation.data, HTTPStatus.OK


# Put and Delete methods are defined
class ReservationPublishResource(Resource):

    def put(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        reservation.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        reservation.is_publish = False

        return {}, HTTPStatus.NO_CONTENT


# Return data to schema dump (by id)
class MeResource(Resource):

    @jwt_required
    def get(self):
        reservation = Reservation.get_by_id(id=get_jwt_identity())
        return reservation_schema.dump(reservation).data, HTTPStatus.OK

