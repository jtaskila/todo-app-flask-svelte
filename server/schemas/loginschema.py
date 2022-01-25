from marshmallow import Schema, fields

class LoginSchema(Schema):
    name        = fields.String(required = True)
    password    = fields.String(required = True)
