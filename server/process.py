import os
def child():
    print('child ',os.getpid())
    os._exit(0)

i=1
while i<=20:
    childpid = os.fork()  # создает дочерний процесс из родительского, запуск нового параллельного процесс
    if childpid == 0:  # 0 дочерний процесс и числовой идентификатор id процесса нового потомка в родительском процессе
        child()
    else:
        print('parent', os.getgid(),'   ', childpid)
    i+=1