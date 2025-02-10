# client.py

import asyncio
import random

import socketio

sio = socketio.AsyncClient()


async def main():
    """
    Connect to the server and then waits for events from it.
    """
    auth = {
        'owner-type': 'SIMPLE',
        'owner': '2974528d-155d-42ed-aa01-37767a1994f8',
        'client': '2974528d-155d-42ed-aa01-37767a1994f7',
    }
    await sio.connect("ws://localhost:8020/", auth=auth, transports=['websocket'], )

    # while True:
    #     await sio.emit("set_name", random.choice(("John", "Mike", "Bob")))
    #     await asyncio.sleep(1)


@sio.on("server-message")
async def get_from_server(name: str):
    """
    Get `server-message` event from server and print the log.
    """
    print(f"Server acknowledged that `{name}` was received.")


@sio.on("connect")
async def handle_connect_ack_from_server():
    """
    The handler will react to successful connection being established.
    """
    await sio.emit("client_update", "Thank you!")



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main()) # you can replace me with `asyncio.run` - doesn't matter.
