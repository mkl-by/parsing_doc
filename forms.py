from wtforms import SelectField, StringField, SubmitField, validators, DateField, Label, TextField, PasswordField
from wtforms.validators import ValidationError
#from wtforms.fields.html5 import DateField
from flask_wtf import FlaskForm, Form

class Form_login(FlaskForm):
    username = StringField('Имя:', validators=[validators.required()])
    #email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    passw = PasswordField('Пароль:', validators=[validators.required(), validators.Length(min=3, max=35)])
    submint = SubmitField('Найти')