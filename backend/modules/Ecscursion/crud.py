from typing import List, Optional

from models import *
from schemas import *

from modules.User.crud import *


async def create_question(q: QuestionCreate) -> QuestionModel:
    new_q = QuestionModel(
        title=q.title,
        answers=q.answers,
        correct_answers=q.correct_answers
    )
    await new_q.create()

    return new_q


async def get_question(id) -> Optional[QuestionModel]:
    q = await QuestionModel.get(id=id)

    return q


async def create_ecscursion_part(ep: EcscursionPartCreate) -> EcscursionPartModel:
    test = []
    for id in ep.test_ids:
        test.append(await get_question(id))
    new_ep = EcscursionPartModel(
        title=ep.title,
        audio=ep.audio,
        materials=ep.materials,
        is_test=ep.is_test,
        test=test
    )
    await new_ep.create()

    return new_ep


async def get_ecscursion_part(id: str) -> Optional[EcscursionPartModel]:
    ep = await EcscursionPartModel.get(id=id)

    return ep


async def create_ecscursion(e: EcscursionCreate) -> EcscursionModel:
    parts = []
    for id in e.parts_ids:
        parts.append(await get_ecscursion_part(id))

    author = await get_user(e.author_id)

    if not author:
        raise Exception("no author!!!")

    new_e = EcscursionModel(
        author=author,
        title=e.title,
        description=e.description,
        preview_img=e.preview_img,
        need_time=e.need_time,
        distance=e.distance,
        route_url=e.route_url,
        parts=parts
    )

    await new_e.create()

    return new_e


async def get_ecscursion(id: str) -> Optional[EcscursionModel]:
    e = await EcscursionModel.get(id=id)

    return e


async def get_all_ecscursions() -> List[EcscursionModel]:
    es = await EcscursionModel.find()

    return es


async def edit_ecscursion(id: str, eu: EcscursionUpdate) -> EcscursionModel:
    e = await EcscursionModel.get(id=id)
    if not e:
        raise Exception("no such excursion")

    e.title = eu.title
    e.description = eu.description
    e.preview_img = eu.preview_img
    e.need_time = eu.need_time
    e.distance = eu.distance
    e.route_url = eu.route_url

    if eu.parts_ids:
        parts = []
        for id in eu.parts_ids:
            parts.append(await get_ecscursion_part(id))
        e.parts = parts

    await e.update()

    return e
