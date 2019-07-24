#7/24/2019
#Forms for the website

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#Import some validator classes so we can validate the input data
from wtforms.validators import DataRequired, Length


#Create a form so the users can add fortunes to the database
class AddFortuneForm(FlaskForm):
    #DECIDE: validate length?
    fortune = StringField('Add a new fortune', validators=[DataRequired()])

    submit = SubmitField('Add Fortune')
