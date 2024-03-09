from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode=True
