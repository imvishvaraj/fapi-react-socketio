import socketio


sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio,
    socketio_path='sockets'
)


@sio.event
async def connect(sid, environ, auth):
    print(f"user {sid} connected")


@sio.event
async def disconnect(sid):
    print(f"user {sid} disconnected")

