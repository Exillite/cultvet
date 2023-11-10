from typing import List, Optional

from models import *
from schemas import *

from modules.User.crud import *
from modules.Ecscursion.crud import *


async def create_ecscursion_pass(ep: PassEcscursionCreate) -> PassEcscursionModel:
    user = await get_user(ep.user_id)
    e = await get_ecscursion(ep.ecscursion_id)

    if not user:
        raise Exception("No user!!!")
    if not e:
        raise Exception("No ecscursion!!!")

    new_ep = PassEcscursionModel(
        user=user,
        ecscursion=e,
        is_finished=False,
        start_time=ep.start_time,
        finish_time=None,
        correct_answers=0,
        points=0,
    )

    await new_ep.create()

    return new_ep


async def get_ecscursion_pass(id: str) -> Optional[PassEcscursionModel]:
    ep = await PassEcscursionModel.get(id=id)

    return ep


async def get_ecscursion_passes_by_user(user_id: str) -> List[PassEcscursionModel]:
    eps = await PassEcscursionModel.find(user_id=user_id)

    return eps


async def edit_ecscursion_pass(id: str, epu: PassEcscursionUpdate) -> PassEcscursionModel:
    ep = await PassEcscursionModel.get(id=id)
    if not ep:
        raise Exception("No ecscursion pass!!!")

    if epu.is_finished:
        ep.is_finished = epu.is_finished
        ep.finish_time = epu.finish_time
        ep.points = 100
    if epu.correct_answers:
        ep.correct_answers = epu.correct_answers

    await ep.update()

    return ep


async def add_ecscursion_pass_correct_answer(id: str, addca: PassEcscursionAddCorrectAnswers) -> PassEcscursionModel:
    ep = await PassEcscursionModel.get(id=id)
    if not ep:
        raise Exception("No ecscursion pass!!!")

    ep.correct_answers += addca.add_correct_answers

    await ep.update()

    return ep
