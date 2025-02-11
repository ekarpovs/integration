# client.py

import asyncio
import sys
import socketio
import uuid
import os
from dotenv import load_dotenv


load_dotenv()

owner_type = os.getenv('OWNER_TYPE', 'SIMPLE')
owner = os.getenv('OWNER', '2974528d-155d-42ed-aa01-37767a1994f8')
bs_url= os.getenv('BROADCAST_SERVICE_URL', 'ws://127.0.0.1:8020')
sio_path = os.getenv('SIO_PATH', '/ws/socket.io')
transports = os.getenv('TRANSPORTS', ['websocket', 'polling', 'webtransport']) 

sio = socketio.AsyncClient()


async def main():
    """
    Connect to the server and then waits for events from it.
    """
    auth = {
        'owner-type': owner_type,
        'owner': owner,
        'client': str(uuid.uuid1()),
    }
    await sio.connect(bs_url, socketio_path=sio_path, auth=auth, transports=['websocket', 'polling', 'webtransport'])

    try:
        while True:
            await asyncio.sleep(3)
    except asyncio.CancelledError:
        print('stop with `CancelledError`')
        sys.exit()


@sio.on("server-message")
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
