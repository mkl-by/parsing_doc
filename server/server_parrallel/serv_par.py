from socket import *
import time
import os
sock=socket(AF_INET, SOCK_STREAM) #создаем объект сокета, в данном случае ТСП/ИП
sock.bind(('', 50008)) #привязываемся к порту
print('Connect...')
sock.listen(5) #организовываем 5 подключений

def now():
    return time.ctime(time.time())

activeChildren=[]

def delChildren():
    while activeChildren:
        pid, stat=os.waitpid(0, os.WNOHANG) #0 проверяет и завершает любой завершившийся дочерний процесс, WNOHANG не дает завершить не завершившийся процесс
        print('pid', pid, '-stat-', stat) #pid идентификатор дочернего процесса
        if not pid: break
        print(activeChildren)
        activeChildren.remove(pid)
        print(activeChildren)

def handleClient(connect): #дочерний процесс
    time.sleep(5)
    while True:
        data = connect.recv(1024)  # получаем данные пока не закончатся
        if not data: break
        connect.send(b'Eho=' + data) #отправляем данные обратно клиенту
    connect.close()



def dispetcher():
    while True:
        connect, adress=sock.accept() # получаем запрос клиента
        print('Serv connected by ', adress, end='')
        print('at', now())
        delChildren() #функция убирает завершившиеся процессы
        childpid=os.fork() #создает дочерний процесс из родительского, запуск нового параллельного процесс
        if childpid==0:  #0 дочерний процесс и числовой идентификатор id процесса нового потомка в родительском процессе
            handleClient(connect)
            print('child==0')
        else:
            print('child!=0')
            activeChildren.append(childpid) #добавить в список активных потомков

dispetcher()