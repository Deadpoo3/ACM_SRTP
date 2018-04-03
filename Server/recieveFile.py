import socketserver
import socket

# Format: name_len      --- one byte
#         name          --- name_len bytes
#         data          --- variable length
# Save data to name into current directory

addr = ('223.3.91.248', 1235)
class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        name_len = ord(self.rfile.read(1))
        name = self.rfile.read(name_len)
        print("Get request:%s" % name)
        fd = open(name, 'w')
        cont = self.rfile.read(4096)
        while cont:
            fd.write(str(cont))
            cont = self.rfile.read(4096)
        fd.close()
        print("Out :%s" % name)


server = socketserver.TCPServer(addr, MyTCPHandler)
server.serve_forever()
