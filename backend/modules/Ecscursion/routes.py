from fastapi import APIRouter

import crud
from schemas import *

router = APIRouter(
    prefix="/api/excursions",
    responses={404: {"description": "Not found"}},
    tags=["Ecscursions"],
)


@router.get("/")
async def get_excursions():
    try:
        ecs = await crud.get_all_ecscursions()
        return {"ecscursions": [e.to_json() for e in ecs]}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.get("/{id}")
async def get_excursion(id: str):
    try:
        e = await crud.get_ecscursion(id)
        return {"ecscursion": e.to_json() if e else None}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.post("/")
async def create_excursion(excursion: EcscursionCreate):
    try:
        e = await crud.create_ecscursion(excursion)
        if e:
            return {"status": 200, "ecscursion": e.to_json()}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.put("/{id}/add_part")
async def add_part(id: str, part: EcscursionPartCreate):
    try:
        new_part = await crud.create_ecscursion_part(part)
        e = await crud.get_ecscursion(id)
        if not e:
            raise Exception("no ecscursion!!!")
        e.parts.append(new_part)
        await e.update()
        return {"status": 200, "ecscursion": e.to_json()}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.put("/part/{id}/add_question")
async def add_qestion(id: str, q: QuestionCreate):
    try:
        new_q = await crud.create_question(q)
        p = await crud.get_ecscursion_part(id)
        if not p:
            raise Exception("no part!!!")
        p.is_test = True
        p.test.append(new_q)
        await p.update()
        return {"status": 200, "ecscursion": p.to_json()}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.put("/{id}")
async def update_ecscursion(id: str, ecscursion: EcscursionUpdate):
    try:
        e = await crud.edit_ecscursion(id, ecscursion)

        return {"status": 200, "ecscursion": e.to_json()}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}
