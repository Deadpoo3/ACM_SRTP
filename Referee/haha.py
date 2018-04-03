import os
import socketserver

# Format: name_len      --- one byte
#         name          --- name_len bytes
#         data          --- variable length
# Save data to name into current directory
addr = ('223.3.91.210', 1234)


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        name_len = ord(self.rfile.read(1))
        name = self.rfile.read(name_len)
        print("Get request:%s" % name)
        path="/home/duyiming/player"
        try:
            os.mkdir(path)
        except:
            print(23)
        name=str(name).strip('b')
        print(name)
        name=name.strip('\'')
        fd = open(path + '/' + name, 'w')
        cont = self.rfile.read(4096)
        while cont:
            fd.write(str(cont))
            cont = self.rfile.read(4096)
        fd.close()
        print("Out :%s" % name)

server = socketserver.TCPServer(addr, MyTCPHandler)
server.serve_forever()