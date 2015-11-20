# via https://github.com/dabeaz/curio/blob/master/examples/bench/torecho.py
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer

from constants import SIMPLE_HTTP_RESPONSE


class EchoServer(TCPServer):
    def handle_stream(self, stream, address):
        self._stream = stream
        try:
            self._stream.read_until_close(None, self.handle_read)
            self._stream.write(SIMPLE_HTTP_RESPONSE)
        except StreamClosedError:
            pass

    def handle_read(self, data):
        # self._stream.write(data)
        pass

if __name__ == '__main__':
    server = EchoServer()
    server.bind(8000)
    server.start(1)
    print("listen on 0.0.0.0:8000")
    IOLoop.instance().start()
    IOLoop.instance().close()
