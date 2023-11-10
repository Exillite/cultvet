from fastapi import APIRouter

import crud
from schemas import *


router = APIRouter(
    prefix="/api/users",
    responses={404: {"description": "Not found"}},
    tags=["User"],
)


@router.post("/register")
async def register(uc: UserCreate):
    try:
        await crud.create_user(uc)
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.get("/{user_id}")
async def get_user(user_id: str):
    try:
        u = await crud.get_user(user_id)
        if u:
            return {"user": u.to_json()}
        else:
            return {"user": None}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@router.get("/tg/{tg_id}")
async def get_user_by_tg_id(tg_id: int):
    try:
        return await crud.get_user_by_tg_id(tg_id)
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}
