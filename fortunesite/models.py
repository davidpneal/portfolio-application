#7/26/2019
from fortunesite import db


class Fortune(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.content}"
