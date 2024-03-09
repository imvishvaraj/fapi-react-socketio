import time
import datetime
import socketio
import asyncio

sio_client = socketio.AsyncClient()

@sio_client.event
async def connect():
    print("connected to server")


@sio_client.event
async def disconnect():
    print("disconnected from server")


@sio_client.event
async def message(data):
    print(f"Received data: {str(data)}")


async def main():
    header = {"Authorization": 'Bearer "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY1NWU0ZDkxOGE0ODY0YWQxMzUxMDViYmRjMDEwYWY5Njc5YzM0MTMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY2FyYm9uLTM1NTUxNSIsImF1ZCI6ImNhcmJvbi0zNTU1MTUiLCJhdXRoX3RpbWUiOjE2NzQwNDU2ODgsInVzZXJfaWQiOiJTZEFmUjJwNXVLWUZtWXM2Y29ITkh6Y01jRGMyIiwic3ViIjoiU2RBZlIycDV1S1lGbVlzNmNvSE5IemNNY0RjMiIsImlhdCI6MTY3NDA0NTY4OCwiZXhwIjoxNjc0MDQ5Mjg4LCJlbWFpbCI6InZpc2h2YXJhai5kaGFuYXdhZGVAd2FsdGxhYnMuaW8iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsidmlzaHZhcmFqLmRoYW5hd2FkZUB3YWx0bGFicy5pbyJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.CmjhGs-AW8WkQGeMG3nl8nEooPnYN__Mnrs54JSwyC7dnis9nNZt2hA3Mpik1-G_zout3y7wNT6AGeCQVMc2KsJdKCOY0EJyCUsyRVxaClxOM5Q12RwSLBebxcnTFzwc5diKi1oklonS9h2a9MqR4gJ1iMjx-se7fLKR-z_G5rR_Pmg5-yWAnVMHTCDwRWYqEM2z83egaUavVBzj2ZcIETp2oeCYa8FzwEQk0JHsdcw_FfmbXSxmIAYrshmJlWOdjL1P5d1LyqpwBsQE664OAj1ur0rs3ssIH9xZZCL39hKTeYGnimt5aVruMRWj4iJp65xb6_qy8kFuA-cd0aBqFg"'}
    # await sio_client.connect(url='http://0.0.0.0:8000', socketio_path='sockets', wait_timeout=10)
    await sio_client.connect(url='http://192.168.0.190:5011', socketio_path='/api/notifications/open_connection', wait_timeout=10, headers=header)

    await sio_client.wait()
    # while sio_client.connected:
    #     time.sleep(1)
    #     print(f"client: {datetime.datetime.now()}")
    #     await sio_client.
    # await sio_client.disconnect()

try:
    asyncio.run(main())
except:
    pass
