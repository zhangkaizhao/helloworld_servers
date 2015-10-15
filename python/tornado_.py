from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer


class Server(TCPServer):
    @coroutine
    def handle_stream(self, stream, address):
        try:
            yield stream.read_bytes(1024, partial=True)
            yield stream.write(b'HTTP/1.0 200 OK\r\n\r\nHello, world!')
        finally:
            stream.close()


server = Server()
server.bind(8000)
server.start(1)
IOLoop.current().start()
