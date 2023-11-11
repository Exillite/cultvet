from pydantic import BaseModel
from typing import List, Optional

from modules.User.schemas import User

# _______________________Question_______________________


class Question(BaseModel):
    id: str
    title: str
    answers: List[str]
    correct_answers: List[str]


class QuestionCreate(BaseModel):
    title: str
    answers: List[str]
    correct_answers: List[str]


class QuestionUpdate(BaseModel):
    title: str
    answers: List[str]
    correct_answers: List[str]


# _______________________EcscursionPart_______________________

class EcscursionPart(BaseModel):
    id: str
    title: str
    audio: str
    materials: List[str]
    is_test: bool
    test: List[Question]


class EcscursionPartCreate(BaseModel):
    title: str
    audio: str
    materials: List[str]
    is_test: bool
    test_ids: List[str]


class EcscursionPartUpdate(BaseModel):
    title: str
    audio: str
    materials: List[str]
    is_test: bool
    test_ids: List[str]


# _______________________Ecscursion_______________________

class Ecscursion(BaseModel):
    id: str
    author: User
    title: str
    description: str
    preview_img: str
    need_time: int
    distance: int
    route_url: str
    parts: List[EcscursionPart]


class EcscursionCreate(BaseModel):
    author_id: str
    title: str
    description: str
    preview_img: str
    need_time: int
    distance: int
    route_url: str
    parts_ids: List[str]


class EcscursionUpdate(BaseModel):
    title: str
    description: str
    preview_img: str
    need_time: int
    distance: int
    route_url: str
    parts_ids: Optional[List[str]]
