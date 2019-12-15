from flask import Blueprint, render_template, redirect, request
from models import Document
from .forms import Myform, Myformdata, MyFormDataRange
from .class_search import Search_document
from flask_paginate import Pagination, get_page_parameter
#from flask import json, jsonify
# from app import csrf
# form.spisok.choices=[(1,1),(2,2),(3,3)]1
# form.spisok.choices=[(i.id, i.number) for i in post]1

a=['по номеру', 'по названию', 'по дате']
search=Blueprint('search', __name__, template_folder='templates')

def searr():
    #бесполезная штука
    s=request.args.get('sear')
    if s==a[0] or s==a[1]:
        sear=s
    else:
        sear = a[int(request.args.get('sear'))] #достаем из реквеста номер
    return sear

@search.route('/', methods=('GET', 'POST'))
def index():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1) #готовим номер страницы
    print('!!!!!!! ', get_page_parameter(),' ', page)
    qq=Search_document()
    form = Myform()
    sear=searr()
    #page = request.args.get('page') #номер страницы
    #print(request.values)
    total=request.args.get('total')
    if request.method == 'POST':
        text=form.number_form.data.strip() #!!!!!!!!!удалить пробелы вконце и начале текста
        if sear==a[0] or sear==a[1]:
            post=qq.get_search_doc(text)
        # totl=post.query.count()
        # href = './?sear={1}&page={0}&total={2}'.format(page, sear, text)
        #pagination = Pagination(page=page, total=totl, css_framework='foundation', search=search, record_name='post', per_page=10)

        return render_template ('search/index_template.html', form=form, post=post, sear=sear)

    post = qq.get_all(page)
    pagination = Pagination(page=page, total=post.query.count(), css_framework='foundation', search=search, record_name='post', per_page=10)
    return render_template('search/index_template.html', pagination=pagination, post=post, form=form, sear=sear) #в папке templates/search/index.html

@search.route('/data', methods=('GET', 'POST'))
def indexdata():
    #поиск документа по дате
    form1=Myformdata()
    q=Search_document()
    sear = a[int(request.args.get('sear'))] #достаем из реквеста номер
    post = q.get_all()
    if form1.validate_on_submit():
        text=form1.date_doc.data
        post=q.get_search_data(text)
        return render_template('search/index_template_date.html', form1=form1, post=post, sear=sear)
    return render_template('search/index_template_date.html', form1=form1, post=post, sear=sear)

@search.route('/datarange', methods=('GET', 'POST'))
def indexdatarange():
    #поиск документа в диапазоне дат
    formrange = MyFormDataRange()
    q = Search_document()
    post = q.get_all()
    if formrange.validate_on_submit():
        post = q.get_search_range_data(formrange.data_one.data, formrange.data_two.data)
        return render_template('search/index_template_date.html', form1=formrange, post=post, sear='в диапазоне дат')
    return render_template('search/index_template_date.html', form1=formrange, post=post, sear='в диапазоне дат')