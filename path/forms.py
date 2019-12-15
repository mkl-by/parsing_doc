from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, validators, DateField

class MyForm(FlaskForm):

    submin = SubmitField('')