from config import app,db
from datetime import datetime

class Votos(db.Model):
    __tablename__ = 'votos'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    vt_s = db.Column(db.String(10), nullable=False)
    vt_n = db.Column(db.String(10), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.now())

    def __init__(self, vt_s, vt_n, date):
        self.vt_s = vt_s
        self.vt_n = vt_n
        self.date = date

    

