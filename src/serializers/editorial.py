from marshmallow import Schema, fields


class EditorialSerializer(Schema):
    id = fields.Int()
    name = fields.Str()
    address = fields.Str()
    city = fields.Str()
    state = fields.Str()
    country = fields.Str()
    website = fields.Str()
