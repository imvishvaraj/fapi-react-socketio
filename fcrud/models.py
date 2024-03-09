from database import Base
from sqlalchemy import Boolean, Column, Integer, String, DATETIME


class Users(Base):
    __tablename__ = "fcrud_users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(100))
    password = Column(String(100))
