from typing import Optional

from modules.User.models import *
from modules.User.schemas import *


async def create_user(user: UserCreate) -> UserModel:
    new_user = UserModel(tg_id=user.tg_id)
    await new_user.create()

    return new_user


async def get_user(id: str) -> Optional[UserModel]:
    user = await UserModel.get(id=id)

    return user


async def get_user_by_tg_id(tg_id: int) -> Optional[UserModel]:
    user = await UserModel.get(tg_id=tg_id)

    return user
