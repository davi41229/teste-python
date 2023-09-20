from config import app,db

from datetime import datetime

class Votos(db.Model):
    __tablename__ = 'votos'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    voto = db.Column(db.String(3))
    date = db.Column(db.DateTime(), default=datetime.now())

    def __init__(self, voto):
        self.voto = voto
    

    

