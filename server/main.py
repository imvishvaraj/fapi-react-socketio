import uvicorn
from fastapi import FastAPI

from sockets import sio_app


app = FastAPI()
app.mount("/", sio_app)


# @app.router("/")
# async def home():
#     return {"message": "Hello Developers"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
