from src.app import db


class Editorial(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(60), nullable=True)
    state = db.Column(db.String(30), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    website = db.Column(db.String(255), nullable=True)

    def from_json(self, **kwargs):
        self.name = kwargs.get('name')
        self.address = kwargs.get('address')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.country = kwargs.get('country')
        self.website = kwargs.get('website')

    def __str__(self):
        return self.name
