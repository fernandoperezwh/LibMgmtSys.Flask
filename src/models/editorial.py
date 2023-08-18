from src.app import db

class Editorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    website = db.Column(db.String(255))

    books = db.relationship('Book', back_populates='editorial')

    def __str__(self):
        return self.name
