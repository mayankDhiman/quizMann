from flask import render_template
from app import app
from app.forms import SetQuizForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/addquiz')
def createQuiz():
    form = SetQuizForm()
    return render_template('addQuiz.html', form=form)
