from wtforms import SelectField, StringField, SubmitField, validators, DateField, Label
from wtforms.validators import ValidationError
#from wtforms.fields.html5 import DateField
from flask_wtf import FlaskForm, Form
from datetime import date
import re

def my_regex_check(form, field):
    #reg = r'^[0-3][0-9][./-][0,1][0-2][./-][1-2][0,9]\d\d$'
    reg=r'^[1-2][0,9]\d\d[./-][0,1][0-2][./-][0-3][0-9]$'
    p=re.compile(reg)
    if not (p.search(str(field.data))) and str(field.data)!='':
         raise ValidationError('Недопустимая дата.\n\n Повторите ввод')

def my_range_check(form, field):
    try:
        if (form.data_one.data > form.data_two.data):
            raise ValidationError('Дата начала интервала поиска должна быть меньше даты окончания.\n\nПовторите ввод!')
    except TypeError:
        raise ValidationError('Заполните все поля!')
        #return False
    # else:
    #     return True
    #
class Myform(FlaskForm):
    spisok=SelectField('docname', [validators.DataRequired()])
    number_form=StringField('number', [validators.DataRequired(), validators.Length(max=10)])

class MyFormDataRange(FlaskForm):
    data_one=DateField('',  [my_regex_check], format='%d.%m.%Y')
    data_two=DateField('',  [my_regex_check, my_range_check], format='%d.%m.%Y')
    submin = SubmitField('Найти')
    # def validate_on_submit(self):
    #     result=super().validate()
    #     if (self.data_one.data>self.data_two.data):
    #         raise ValidationError('Дата начала интервала поиска должна быть меньше даты окончания\n\nПовторите ввод')
    #         return False
    #     else:
    #         return result

class Myformdata(FlaskForm):
    date_doc=DateField('Формат ввода дд.мм.гггг',  [my_regex_check], format='%d.%m.%Y')
    submin=SubmitField('Найти')
    #date_doc=DateField('Ведите данные', [validators.DataRequired(), validators.regexp('(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d', 1, 'sdsdsd')], format='%d.%m.%Y')

    # def validate_on_submit(self):
    #         result=super().validate()
    #         reg = r'^[1-2][0,9]\d\d[./-][0,1][0-2][./-][0-3][0-9]$'
    #         p=re.compile(reg)
    #         if not p.search(str(self.date_doc.data)):
    #             return False #raise ValidationError('Повторите ввод')
    #         else:
    #             return result
            # if (p.self.date_doc.data>self.enddate.data):
            #     return False
            # else:
            #     return result

