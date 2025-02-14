// @ts-nocheck

// Configuration 
const BEBS_LOCATOR = 'http://127.0.0.1:8020';
const ROOT_PATH = '/ws/socket.io';
const TRANSPORTS = ['websocket', 'polling'];
const NAMESPACE = 'test';
const ROOM = '2974528d-155d-42ed-aa01-37767a199fff';
const CLIENT =  Date.now().toString(36) + Math.random().toString(36).substring(2);
const RECONNECTION_ATTEMPTS =  5

const cfg = document.getElementById('cfg');

function showConfiguration( ) {
  cfg.innerText = `Server URL: ${BEBS_LOCATOR}`;
  cfg.innerText += `\n PathRoot: ${ROOT_PATH}`;
  cfg.innerText += `\n Transports: ${TRANSPORTS}`;
  cfg.innerText += `\n Namespace: ${NAMESPACE}`;
  cfg.innerText += `\n Room: ${ROOM}`;
  cfg.innerText += `\n Client: ${CLIENT}`; 
  cfg.innerText += `\n reconnectionAttempts: ${RECONNECTION_ATTEMPTS}`; 
}


const eventLog = document.getElementById('eventLog');

function updateEventLog(message) {
  eventLog.innerText += `\n${message}`;
}

// Initialize WebSocket connection with the authData
async function initializeSocket() {
//   const authData = await getAuthData();

  // console.log(authData);  // Ensure authData is fetched correctly
  const authData = {
    'owner-type': NAMESPACE,
    'owner': ROOM,
    'client': CLIENT,
  };
  const namespace = `/${NAMESPACE}`

  // Assign the socket object to the global variable
  const sio = io(`${BEBS_LOCATOR}${namespace}`, { 
      path: `${ROOT_PATH}${namespace}`,
      reconnectionAttempts: RECONNECTION_ATTEMPTS,
      auth: authData,
      transports: TRANSPORTS
  });

// Add event listeners
  // Handle connection
  sio.on('connect', () => {
    const mess = 'Connected to the server';
    console.log(mess);
    updateEventLog(mess);
    const room = ROOM; // Update this with your room name
    sio.emit('join_room', room);
  });

  // Handle successful room join
  sio.on('room_joined', (room) => {
    const mess = `Joined room: ${room}`;
    console.log(mess);
    updateEventLog(mess);
  });

  // Handle room left
  sio.on('room_left', (room) => {
    const mess = `Left room: ${room}`;
    console.log(mess);
    updateEventLog(mess);
    sio.disconnect();
  });

  // Handle server message
  sio.on('server-message', (data) => {
    const mess = `The message: '${data}' was received from the server.`;
    console.log(mess);
    updateEventLog(mess);
    if (data === 'cancel') {
        sio.emit('leave_room');
  }
  });

  // Handle connection error
  sio.on('connect_error', (error) => {
    const mess = `connect error '${error}'`;
    console.error(mess);
    updateEventLog(mess);
  });

  // Handle disconnection
  sio.on('disconnect', (reason) => {
    const mess = `Disconnected from the server by the reason '${reason}'`;
    console.log(mess);
    updateEventLog(mess);
    sio.emit('leave_room');
  });

  return sio;
}
showConfiguration();
initializeSocket();
