from builtins import enumerate

from flask import Blueprint, render_template, request
from pathlib import Path, PurePath
from path.forms import MyForm
from docx import Document

paths=Blueprint('paths', __name__, template_folder='templates')
path_home = Path.home()
expansion=['.doc', '.docx']
dat=['номер документа', 'экземпляр', 'наименование документа', 'страницы']
pars=('дело', 'том')

def parsing_doc(path):
    q=['-','', ' ']
    d={}
    document = Document(path)

    for para in document.paragraphs:
        #выбираем все параграфы(строки) из документа и построчно читаем
        par=para.text
        num1=par.find('дело')
        num2 = par.find('том')
        if num1!=-1 or num2!=-1:
            #если в стоку входят слова "дело" или "том"
            spl=par.split()
            for st, spis in enumerate(spl):
                if spis.isdigit() and spl[st-1]=='дело':
                    case_number=int(spis)
                elif spis.isdigit() and spl[st-1]=='том':
                    case_tom=int(spis)

    for table in document.tables:
        #разбираем таблицу сначала на таблицы, потом на строки, потом поячеячно
        for s, row in enumerate(table.rows):
            dd={}
            sss=0
            for ss, i in enumerate(row.cells):
                if s >= 3 and not(i.text in q) and ss!=0:
                    e=i.text
                    dd[dat[sss]]=e
                    sss+=1
            dd['дело']=case_number
            dd['том']=case_tom
            if s>=3: d[s-3]=dd

    print(d)

@paths.route('/', methods=['GET', 'POST'])
def my_path():
    form = MyForm()
    pren = str(path_home)
    if form.validate_on_submit():
        p=Path(request.form['form_s'])
        parsing_doc(p)

    directory = []
    files_dict={}

    path_isdir = Path.iterdir(path_home) # директория в которой ищем,
    p=request.args.get('urr')

    if p:
        path_isdir = Path.iterdir(Path(p))
        pren=str(Path(p).parent)# путь папка назад
    #[dd.append(x.name) for x in path_home.iterdir() if x.is_file() and (x.suffix in expansion)]

    for i in path_isdir:
        if i.is_file() and (i.suffix in expansion): #если файл и расширение ".doc", "docx","txt"
            files_dict[i.name]=i #добавляем в словарь имя файла как ключ и путь к нему
        elif i.is_dir() and not (i.parts[-1:][0].startswith('.')): #если директория и начинается на "."
            directory.append(i)

    return render_template('path/route.html', path_isdir=directory, form=form, pren=pren, files_dict=files_dict)
