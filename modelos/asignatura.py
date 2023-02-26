from config import db
from sqlalchemy.sql import func

class Asignatura(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    profesor = db.Column(db.String(255))
    asignatura = db.Column(db.String(255))
    img = db.Column(db.String(255))

    def __init__(self, profesor, asignatura, img):
        self.profesor=profesor
        self.asignatura=asignatura
        self.img = img
    def __repr__(self):
        return f'{self.asignatura}'