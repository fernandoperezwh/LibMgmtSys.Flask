from src.app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.Date)
    cover = db.Column(db.String)

    authors = db.relationship('Author', secondary='book_author', back_populates='books')
    editorial_id = db.Column(db.Integer, db.ForeignKey('editorial.id'))
    editor = db.relationship('Editorial', back_populates='books')

    def __str__(self):
        return self.title
