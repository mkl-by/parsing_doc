from http.server import HTTPServer,CGIHTTPRequestHandler
server_addr=('', 9000)
httpd=HTTPServer(server_addr, CGIHTTPRequestHandler)
httpd.serve_forever()
