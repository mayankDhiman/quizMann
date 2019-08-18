from flask import *
from app import app, db
from app.forms import SetQuizForm
from app.models import Questions


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/addquiz', methods=['GET', 'POST'])
def createQuiz():
    form = SetQuizForm()
    if form.validate_on_submit():
        newQuiz = Questions(question=form.O_question1.data, optionA=form.A_question1.data, optionB=form.B_question1.data, optionC=form.C_question1.data, optionD=form.D_question1.data)
        db.session.add(newQuiz)
        db.session.commit()
        return redirect('/index')
    return render_template('addQuiz.html', form=form)
