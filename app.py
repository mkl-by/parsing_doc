from flask import Flask

from config import Configuration
# from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
#from search.blueprint import search
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# from flask_wtf.csrf import CSRFProtect
# from flask_session import Session

app = Flask(__name__) #__name__ имя текущего файла
Bootstrap(app)

app.config.from_object(Configuration) #метод from_object позволяет наполнять словарь config

db=SQLAlchemy(app)


migrate=Migrate(app, db) #создаем миграции между версией арр и базой данных
manager=Manager(app)
manager.add_command('db', MigrateCommand) #Создаем команду db для мигаций


# регистрируем отдельное приложение
from search.blueprint import search
from path.path_bluprint import paths
app.register_blueprint(search, url_prefix='/search') #регистрируем отдельное приложение
app.register_blueprint(paths, url_prefix='/path') #регистрируем второе приложение
