from app import db

class Highscore(db.Model):
    __tablename__ = "ShibaChefHighscore"

    id = db.Column(db.Integer, primary_key = True)
    highscore = db.Column(db.Integer)

    def __init__(self, id, highscore):
        self.id = id
        self.highscore = highscore