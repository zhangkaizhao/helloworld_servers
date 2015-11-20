from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer

from constants import SIMPLE_HTTP_RESPONSE


class Server(TCPServer):
    @coroutine
    def handle_stream(self, stream, address):
        try:
            yield stream.read_bytes(1024, partial=True)
            yield stream.write(SIMPLE_HTTP_RESPONSE)
        except StreamClosedError:
            pass
        finally:
            stream.close()


server = Server()
server.bind(8000)
server.start(1)
print("listen on 0.0.0.0:8000")
IOLoop.current().start()
