from fastapi import APIRouter

import crud
from schemas import *

router = APIRouter(
    prefix="/api/excursionspass",
    responses={404: {"description": "Not found"}},
    tags=["Excursions Pass"],
)


@router.post("/")
async def create_excursionspass(excursionspass: PassEcscursionCreate):
    try:
        ep = await crud.create_ecscursion_pass(excursionspass)
        if ep:
            return {"status": 200, "pass": ep.to_json()}
        else:
            return {"status": 500}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.get("/{id}")
async def get_excursionspass(id: str):
    try:
        ep = await crud.get_ecscursion_pass(id)
        if ep:
            return {"status": 200, "pass": ep.to_json()}
        else:
            return {"status": 500}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.get("/user/{id}")
async def get_user_excursionspass(id: str):
    try:
        eps = await crud.get_ecscursion_passes_by_user(id)
        return {"status": 200, "pass": [ep.to_json() for ep in eps]}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.put("/{id}")
async def update_excursionspass(id: str, excursionspass: PassEcscursionUpdate):
    try:
        ep = await crud.edit_ecscursion_pass(id, excursionspass)
        if ep:
            return {"status": 200, "pass": ep.to_json()}
        else:
            return {"status": 500}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.put("/{id}/correctanswer")
async def update_correctanswer(id: str, addca: PassEcscursionAddCorrectAnswers):
    try:
        ep = await crud.add_ecscursion_pass_correct_answer(id, addca)
        if ep:
            return {"status": 200, "pass": ep.to_json()}
        else:
            return {"status": 500}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}
