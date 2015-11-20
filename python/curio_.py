# via https://github.com/dabeaz/curio/blob/master/examples/bench/curioecho.py
from curio import Kernel, new_task, run_server

from constants import SIMPLE_HTTP_RESPONSE


async def echo_handler(client, addr):
    while True:
        data = await client.recv(1024)
        if not data:
            break
        await client.sendall(SIMPLE_HTTP_RESPONSE)


if __name__ == '__main__':
    print("listen on 0.0.0.0:8000")
    kernel = Kernel()
    kernel.run(run_server('', 8000, echo_handler))
