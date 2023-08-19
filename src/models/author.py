from src.app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(40))
    email = db.Column(db.String(254), nullable=True)  # 254 to be compliant with RFCs 3696 and 5321

    def from_json(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.email = kwargs.get('email')

    def __str__(self):
        return F"{self.last_name} / {self.fist_name}"