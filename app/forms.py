from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SetQuizForm(FlaskForm):
    O_question1 = StringField('Question 1', validators=[DataRequired()])
    A_question1 = StringField('Question 1 (A)', validators=[DataRequired()])
    B_question1 = StringField('Question 1 (B)', validators=[DataRequired()])
    C_question1 = StringField('Question 1 (C)', validators=[DataRequired()])
    D_question1 = StringField('Question 1 (D)', validators=[DataRequired()])

    # _question2 = StringField('Question 2', validators=DataRequired)
    # A_question2 = StringField('Question 2 (A)', validators=DataRequired)
    # B_question2 = StringField('Question 2 (B)', validators=DataRequired)
    # C_question2 = StringField('Question 2 (C)', validators=DataRequired)
    # D_question2 = StringField('Question 2 (D)', validators=DataRequired)

    # _question3 = StringField('Question 3', validators=DataRequired)
    # A_question3 = StringField('Question 3 (A)', validators=DataRequired)
    # B_question3 = StringField('Question 3 (B)', validators=DataRequired)
    # C_question3 = StringField('Question 3 (C)', validators=DataRequired)
    # D_question3 = StringField('Question 3 (D)', validators=DataRequired)

    # _question4 = StringField('Question 4', validators=DataRequired)
    # A_question4 = StringField('Question 4 (A)', validators=DataRequired)
    # B_question4 = StringField('Question 4 (B)', validators=DataRequired)
    # C_question4 = StringField('Question 4 (C)', validators=DataRequired)
    # D_question4 = StringField('Question 4 (D)', validators=DataRequired)

    submit = SubmitField('Add Quiz!')