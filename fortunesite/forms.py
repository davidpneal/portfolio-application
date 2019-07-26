#7/26/2019
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#Create a form so the users can add fortunes to the database
class AddFortuneForm(FlaskForm):
    fortune = StringField('Add a new fortune', validators=[DataRequired()])

    submit = SubmitField('Add Fortune')
