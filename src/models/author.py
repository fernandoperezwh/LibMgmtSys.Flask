from src.app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(254), nullable=True)  # 254 to be compliant with RFCs 3696 and 5321

    book_author = db.Table(
        'book_author',
        db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
        db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
    )

    def __str__(self):
        return F"{self.last_name} / {self.name}"
