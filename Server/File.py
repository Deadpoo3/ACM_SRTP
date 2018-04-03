#!/usr/bin/python
import socketserver

# Format: name_len      --- one byte
#         name          --- name_len bytes
#         data          --- variable length
# Save data to name into current directory
addr = ('192.168.1.108', 3243)


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        name_len = ord(self.rfile.read(1))
        name = self.rfile.read(name_len)
        print("Get request:%s" % name)
        fd = open(name, 'w')
        Cont = self.rfile.read(4096)
        cont=Cont.decode()
        while cont:
            fd.write(cont)
            cont = self.rfile.read(4096)
        fd.close()
        print("Out :%s" % name)


server = socketserver.TCPServer(addr, MyTCPHandler)
server.serve_forever()