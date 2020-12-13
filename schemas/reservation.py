from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError


class ReservationSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Int(dump_only=True)
    date = fields.String(required=True, validate=[validate.Length(max=100)])
    time = fields.Integer(required=True)
    client = fields.String(required=True)
    is_publish = fields.Boolean(dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
