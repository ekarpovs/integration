# client.py

import asyncio
import sys
import socketio
from socketio import exceptions
import uuid
import os
from dotenv import load_dotenv


load_dotenv()

namespace = os.getenv('NAMESPACE', 'test')
room = os.getenv('ROOM', '2974528d-155d-42ed-aa01-37767a1994f8')
client = str(uuid.uuid1())
bs_url= os.getenv('BROADCAST_SERVICE_URL', 'ws://127.0.0.1:8020')
sio_path = os.getenv('SIO_PATH', '/ws/socket.io')
transports = os.getenv('TRANSPORTS', ['websocket', 'polling'])
if isinstance(transports, str):
    transports = [i.strip() for i in transports[1:-1].replace('"',"").split(',')]

reconnection_attempts = int(os.getenv('RECONNECTION_ATTEMPTS', 5) )

print(f'namespace: {namespace}')
print(f'room: {room}')
print(f'client: {client}')
print(f'bs_url: {bs_url}')
print(f'transports: {transports}')
print(f'reconnection_attempts: {reconnection_attempts}')

sio = socketio.AsyncClient(
    reconnection_attempts=reconnection_attempts
)

namespace = f'/{namespace}'

@sio.on("server-message", namespace=namespace)
async def get_from_server(data):
    """
    Get `server-message` event from server and print the log.
    """
    print(f'The message `{data}` was received from the server.')
    if data == 'cancel':
        # Initiate the disconnect event
        await sio.emit('leave_room', namespace=namespace)



@sio.on('connect', namespace=namespace)
async def handle_successful_connect():
    print(f'Connected to the server')
    await sio.emit('join_room', room, namespace=namespace)

@sio.on("connect_error")
async def handle_connect_error(data):
    """
    The handler will react to connection error.
    """
    print(f'connect error `{data}`')


@sio.on('disconnect', namespace=namespace)
async def handle_disconnect():
    print(f'Disconnected from the server')
    await sio.emit('leave_room', namespace=namespace)
                   

@sio.on('room_joined', namespace=namespace)
async def room_joined(room):
    print(f"Joined room: {room}")

@sio.on('room_left', namespace=namespace)
async def room_left(room):
    print(f"Left room: {room}")
    await sio.disconnect()


async def main():
    """
    Connect to the server and then waits for events from it.
    """
    auth = {
        'owner-type': namespace,
        'owner': room,
        'client': client,
    }
    try:
        await sio.connect(bs_url, socketio_path=sio_path, auth=auth, transports=transports, namespaces=[namespace])
    except exceptions.ConnectionError:
        print('Can`t connect to the server')
        exit()

    try:
        await sio.wait()
    except asyncio.CancelledError:
        print('stop due to `CancelledError`')
        sys.exit()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main()) # you can replace me with `asyncio.run` - doesn't matter.
