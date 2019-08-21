from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)




class Questions(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1200), unique=True)
    optionA = db.Column(db.String(200))
    optionB = db.Column(db.String(200))
    optionC = db.Column(db.String(200))
    optionD = db.Column(db.String(200))    
    answer = db.Column(db.String(200))

    def __repr__(self):
        return f"Questions('{self.question}', '{self.optionA}', '{self.optionB}', '{self.optionC}', '{self.optionD}', '{self.answer}')"
