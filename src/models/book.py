from src.app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    publish_date = db.Column(db.Date, nullable=True)
    cover = db.Column(db.String, nullable=True)
    # relations
    # editorial = db.relationship('Editorial')
    # authors = db.relationship('Author', secondary='book_authors')

    def from_json(self, **kwargs):
        self.title = kwargs.get('title')
        self.publish_date = kwargs.get('publish_date')
        self.cover = kwargs.get('cover')

    def __str__(self):
        return self.title


# class BooksAuthors(db.Model):
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
#     author_id = db.Column(db.Integer, db.ForeignKey('author.id'), primary_key=True)
