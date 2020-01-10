from socket import *
import time, os, signal, _thread as thread

sock=socket(AF_INET, SOCK_STREAM) #создаем объект сокета, в данном случае ТСП/ИП
sock.bind(('', 50007)) #привязываемся к порту
print('Connect...')
sock.listen(5) #организовываем 5 подключений

def now():
    return time.ctime(time.time())

def handleClient(connect): #дочерний процесс
    time.sleep(5)
    while True:
        data = connect.recv(1024)  # получаем данные пока не закончатся
        if not data: break
        connect.send(b'Eho=' + data) #отправляем данные обратно клиенту
    connect.close()
    os._exit(0)

def dispetcher():
    while True:
        connect, adress=sock.accept() # получаем запрос клиента
        print('Serv connected by ', adress, end='')
        print('at', now())
        thread.start_new_thread(handleClient, (connect,)) # запускаем поток
dispetcher()