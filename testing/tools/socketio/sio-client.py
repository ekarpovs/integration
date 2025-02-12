# client.py

import asyncio
import sys
import socketio
from socketio import exceptions
import uuid
import os
from dotenv import load_dotenv


load_dotenv()

owner_type = os.getenv('OWNER_TYPE')
owner = os.getenv('OWNER', '2974528d-155d-42ed-aa01-37767a1994f8')
bs_url= os.getenv('BROADCAST_SERVICE_URL', 'ws://127.0.0.1:8020')
sio_path = os.getenv('SIO_PATH', '/ws/socket.io')
transports = os.getenv('TRANSPORTS', ['websocket', 'polling', 'webtransport']) 
transports = [i.strip() for i in transports[1:-1].replace('"',"").split(',')]

reconnection_attempts = int(os.getenv('RECONNECTION_ATTEMPTS', 0) )

sio = socketio.AsyncClient(
    reconnection_attempts=reconnection_attempts
)

namespace = f'/{owner_type}'

@sio.on("server-message", namespace=namespace)
async def get_from_server(data):
    """
    Get `server-message` event from server and print the log.
    """
    print(f'The message `{data}` was received from the server.')
    # if data == 'cancel':
    #     print("stopp via message - `cancel`")
    #     sys.exit()



@sio.on('connect', namespace=namespace)
async def handle_successful_connect():
    print(f"Connected:")
    await sio.emit('join_room', owner, namespace=namespace)

@sio.on("connect_error")
async def handle_connect_error(data):
    """
    The handler will react to connection error.
    """
    print(f'connect error `{data}`')


@sio.on('disconnect', namespace=namespace)
async def handle_disconnect():
    print("Disconnected from server")
    await sio.emit('leave_room', 'room1', namespace=namespace)
                   

@sio.on('room_joined', namespace=namespace)
async def room_joined(room):
    print(f"Joined room: {room}")

@sio.on('room_left', namespace=namespace)
async def room_left(room):
    print(f"Left room: {room}")


async def main():
    """
    Connect to the server and then waits for events from it.
    """
    auth = {
        'owner-type': namespace,
        'owner': owner,
        'client': str(uuid.uuid1()),
    }
    try:
        await sio.connect(bs_url, socketio_path=sio_path, auth=auth, transports=transports, namespaces=[namespace])
    except exceptions.ConnectionError:
        print('Can`t connect to the server')
        await sio.emit('leave_room', owner, namespace=namespace)
        exit()

    try:
        # while True:
        #     await asyncio.sleep(3)
        await sio.wait()
    except asyncio.CancelledError:
        print('stop due to `CancelledError`')
        sys.exit()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main()) # you can replace me with `asyncio.run` - doesn't matter.
