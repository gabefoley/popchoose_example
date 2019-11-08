from app import db


class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    popularity = db.Column(db.Integer)
    image = db.Column(db.String(250))

    def __init__(self, id, name, popularity, image):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.image = image




class MatchUp(db.Model):
    __tablename__ = 'matchup'
    id = db.Column(db.String(500), primary_key=True)
    correct = db.Column(db.Integer)
    incorrect = db.Column(db.Integer)

    def __init__(self, id, correct, incorrect):
        self.id = id
        self.correct = correct
        self.incorrect = incorrect
