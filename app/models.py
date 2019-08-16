from app import db

class Questions(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1200), unique=True)
    optionA = db.Column(db.String(200))
    optionB = db.Column(db.String(200))
    optionC = db.Column(db.String(200))
    optionD = db.Column(db.String(200))
    answer = db.relationship('AnswerKey', backref = 'question', lazy='dynamic')

    def __repr__(self):
        return '<Questions: {}>'.format(self.question)

class AnswerKey(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(200))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def __repr__(self):
        return '<Answer: {}>'.format(self.answer)

