import socket, pickle
for i in range(8):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создаем объект сокета, в данном случае ТСП/ИП
    sock.connect(('127.0.0.1', 50007)) #привязываемся к порту


    sock.send(b'kldjfgl')
    data=sock.recv(1024)
    print('otvet :' ,data)
    sock.close()
