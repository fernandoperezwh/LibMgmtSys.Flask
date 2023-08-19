from marshmallow import Schema, fields


class AuthorSerializer(Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
