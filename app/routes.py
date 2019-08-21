from flask import *
from app import app, db
from app.forms import SetQuizForm, DisplayQuizForm
from app.models import Questions


@app.route('/')
def mainPage():
    db.drop_all()
    db.create_all()
    return render_template('index.html', title="Welcome")

@app.route('/addquiz', methods=['GET', 'POST'])
def createQuiz():
    form = SetQuizForm()
    newQuiz = Questions(question=form.ques.data, optionA=form.A_ques.data, optionB=form.B_ques.data, optionC=form.C_ques.data, optionD=form.D_ques.data, answer=form.answ.data)
    if form.validate_on_submit():
        db.session.add(newQuiz)
        db.session.commit()
        if form.submit.data:            
            return render_template('quizSet.html', form=form)
        elif form.nxt.data:
            return render_template('addQuiz.html', form=form)
    return render_template('addQuiz.html', form=form)


@app.route('/displayQuiz', methods=['GET', 'POST'])
def displayQuiz():
    all_questions = Questions.query.all()
    return render_template('displayQuiz.html', questions = all_questions)
    
@app.route('/postQuiz', methods=['GET', 'POST'])
def postQuiz():
    if request.method == "POST":
        score = 0
        maxScore = Questions.query.count()
        for q_id in range(1, maxScore + 1):
            # print(str(Questions.query.get(q_id).answer), request.form["question_" + str(q_id)], sep="\t")
            if str(Questions.query.get(q_id).answer) == request.form["question_" + str(q_id)]:
                score += 1
    return render_template('result.html', score=score, maxScore=maxScore)







