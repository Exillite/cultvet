from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from modules.User.schemas import User
from modules.Ecscursion.schemas import Ecscursion


class PassEcscursion(BaseModel):
    id: str
    user: User
    ecscursion: Ecscursion
    is_finished: bool
    start_time: datetime
    finish_time: datetime
    correct_answers: int
    points: int


class PassEcscursionCreate(BaseModel):
    user_id: str
    ecscursion_id: str
    start_time: datetime


class PassEcscursionUpdate(BaseModel):
    is_finished: Optional[bool]
    finish_time: Optional[datetime]
    correct_answers: Optional[int]


class PassEcscursionAddCorrectAnswers(BaseModel):
    add_correct_answers: int
