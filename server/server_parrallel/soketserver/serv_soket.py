import socketserver, time
host=''
port=50007

def now():
    return time.ctime(time.time())

class MyClienthandle(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address, now())
        time.sleep(5)
        while True:
            data=self.request.recv(1024)
            if not data: break
            reply = 'Echo=>%s at %s' % (data, now())
            self.request.send(reply.encode())
        self.request.close()

myaddr=(host, port)
server=socketserver.ThreadingTCPServer(myaddr, MyClienthandle) #ветвящийся сервер ForkingTCPServer
server.serve_forever()
