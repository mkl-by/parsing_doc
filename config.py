import os

class Configuration(object):
    DEBUG=True #включение отладочной информации

#path
    basedir = os.path.abspath(os.path.dirname(__file__)) #текущая директория

# session
    #SESSION_TYPE='filesystem'

#секретный ключ
    #WTF_CSRF_ENABLED = True
    CSRF_ENABLED=True
    #WTF_CSRF_SECRET_KEY = 'KiJyftF^&*Ygbv%^eTRYTF$%'
    SECRET_KEY = b'KiJyftkjdfdifTF$%'

#настройки бутстрап
    BOOTSTRAP_SERVE_LOCAL = True #работаем с локальным файлом бутстрап

#настройки SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'basa') #путь к файлу базы
    SQLALCHEMY_TRACK_MODIFICATIONS=True #не излучает сигналы




