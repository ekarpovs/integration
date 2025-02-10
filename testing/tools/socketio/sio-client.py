# client.py

import asyncio
import sys
import socketio

sio = socketio.AsyncClient()


async def main():
    """
    Connect to the server and then waits for events from it.
    """
    auth = {
        'ownertype': 'SIMPLE',
        'owner': '2974528d-155d-42ed-aa01-37767a1994f8',
        'client': '2974528d-155d-42ed-aa01-37767a1994f7',
    }
    await sio.connect('ws://127.0.0.1:8020', socketio_path='/ws/socket.io', auth=auth, transports=['websocket', 'polling', 'webtransport'], )

    try:
        while True:
            await asyncio.sleep(3)
    except asyncio.CancelledError:
        print('stop with `CancelledError`')
        sys.exit()


@sio.on("next")
async def get_from_server(data):
    """
    Get `server-message` event from server and print the log.
    """
    print(f'The message `{data}` was received from the server.')
    if data == 'cancel':
        print("stopp via message - `cancel`")
        sys.exit()



@sio.on("connected")
async def handle_successful_connect(data):
    """
    The handler will react to successful connection being established.
    """
    print(f'connected `{data}`')


@sio.on("connect_error")
async def handle_connect_error(data):
    """
    The handler will react to connection error.
    """
    print(f'connect error `{data}`')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main()) # you can replace me with `asyncio.run` - doesn't matter.
