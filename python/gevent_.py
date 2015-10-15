from gevent.server import StreamServer


class EchoServer(StreamServer):

    def handle(self, socket, address):
        rfile = socket.makefile(mode='rb')
        while 1:
            line = rfile.readline()
            if not line.strip():
                break
        socket.sendall(b'HTTP/1.0 200 OK\r\n\r\nHello, world!')
        rfile.close()


if __name__ == '__main__':
    print('Receiving streams on :8000')
    EchoServer(':8000').serve_forever()
