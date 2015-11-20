from __future__ import print_function

import signal
import pyuv

from constants import SIMPLE_HTTP_RESPONSE


def on_read(client, data, error):
    if data is None:
        client.close()
        clients.remove(client)
        return
    # client.write(data)
    # print(data)
    client.write(SIMPLE_HTTP_RESPONSE)
    client.close()
    clients.remove(client)


def on_connection(server, error):
    client = pyuv.TCP(server.loop)
    server.accept(client)
    clients.append(client)
    client.start_read(on_read)


def signal_cb(handle, signum):
    [c.close() for c in clients]
    signal_h.close()
    server.close()


print("PyUV version %s" % pyuv.__version__)

loop = pyuv.Loop.default_loop()
clients = []

server = pyuv.TCP(loop)
server.bind(("0.0.0.0", 8000))
server.listen(on_connection)
print("listen on 0.0.0.0:8000")

signal_h = pyuv.Signal(loop)
signal_h.start(signal_cb, signal.SIGINT)

loop.run()
print("Stopped!")
