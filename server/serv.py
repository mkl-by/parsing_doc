import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создаем объект сокета, в данном случае ТСП/ИП
sock.bind(('', 50008)) #привязываемся к порту
print('Connect...')
sock.listen(5) #организовываем 5 подключений
while True:
    connect, adress=sock.accept() # получаем запрос клиента
    print('Serv adress ', adress)
    print (connect)
    while True:
        data=connect.recv(1024)  #получаем данные пока не закончатся
        if not data: break
        connect.send(b'Eho='+data)
    connect.close()



