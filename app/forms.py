from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class SetQuizForm(FlaskForm):
    ques = StringField('Question', validators=[DataRequired()])
    A_ques = StringField('(A)', validators=[DataRequired()])
    B_ques = StringField('(B)', validators=[DataRequired()])
    C_ques = StringField('(C)', validators=[DataRequired()])
    D_ques = StringField('(D)', validators=[DataRequired()])
    answ = StringField('Answer', validators=[DataRequired()])
    nxt = SubmitField('More Question!')
    submit = SubmitField('Add Quiz!')

class DisplayQuizForm(FlaskForm):
    QuestionAnswer = RadioField(label="", choices=[("", ""), ("", ""), ("", ""), ("", "")])
    nxt = SubmitField('Next Question!')
    submit = SubmitField('Submit response!')