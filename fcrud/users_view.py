from fastapi import APIRouter, status
from database import conn, session_local
from schemas import User
from models import Users

from sqlalchemy.orm import Session

user = APIRouter()

db = session_local()


@user.get("/")
async def read_data():
    return db.query(Users).all()


@user.get("/{id}")
async def read_data(id: int):
    return db.query(Users).filter(Users.id == id).first()


@user.post("/", response_model=User,
           status_code=status.HTTP_201_CREATED)
async def read_data(user: User):
    new_user = Users(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    return new_user


# @user.put("/{id}")
# async def read_data(id: int, user:User):
#
#     return db.query(Users).filter(Users.id == id).first()


# @user.delete("/{id}")
# async def read_data(id: int):
#     conn.execute(Users.delete().where(Users.c.id == id))
#     return conn.execute(Users.select()).fetchall()
