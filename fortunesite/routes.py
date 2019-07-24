#7/24/2019
from flask import render_template, url_for, flash
from fortunesite import app
from fortunesite.forms import AddFortuneForm
from fortunesite.models import Fortune


@app.route("/")
@app.route("/home")
def index():
    #Get a random fortune from the database
    rand_fortune = 'This is a placeholder fortune.'
    return render_template('home.html', fortune=rand_fortune)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/addfortune", methods=['GET', 'POST'])
def register():
    form = AddFortuneForm()

    if form.validate_on_submit():
        flash('A new fortune has been added!')

    return render_template('addfortune.html', title='Add Fortune', form=form)
