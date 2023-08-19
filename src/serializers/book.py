from marshmallow import Schema, fields


class BookSerializer(Schema):
    id = fields.Int()
    title = fields.Str()
    publish_date = fields.Date()
    cover = fields.Str()
    # TODO: relations
    # editorial = db.relationship('Editorial')
    # authors = db.relationship('Author', secondary='book_authors')
