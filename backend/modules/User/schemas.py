from pydantic import BaseModel


class User(BaseModel):
    id: str
    tg_id: int
    points: int


class UserCreate(BaseModel):
    tg_id: int
