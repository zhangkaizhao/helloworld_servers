from gevent.server import StreamServer

from constants import SIMPLE_HTTP_RESPONSE


class EchoServer(StreamServer):

    def handle(self, socket, address):
        rfile = socket.makefile(mode='rb')
        while 1:
            line = rfile.readline()
            if not line.strip():
                break
        socket.sendall(SIMPLE_HTTP_RESPONSE)
        rfile.close()


if __name__ == '__main__':
    print('Receiving streams on :8000')
    EchoServer(':8000').serve_forever()
