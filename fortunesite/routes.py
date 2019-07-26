#7/26/2019
from flask import render_template, url_for, flash
from fortunesite import app, db
from fortunesite.forms import AddFortuneForm
from fortunesite.models import Fortune
import random


@app.route("/")
@app.route("/home")
def home():
    #Get a random fortune from the database
    rand_fortune = random.choice(Fortune.query.all())
    return render_template('home.html', fortune=rand_fortune)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/addfortune", methods=['GET', 'POST'])
def addfortune():
    form = AddFortuneForm()

    if form.validate_on_submit():
        fortune = Fortune(content=form.fortune.data)
        db.session.add(fortune)
        db.session.commit()
        flash('Your wisdom has been added!')
        form.fortune.data = ""

    return render_template('addfortune.html', title='Add Fortune', form=form)
