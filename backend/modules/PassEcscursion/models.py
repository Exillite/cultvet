from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from bson import ObjectId

from db import db

from modules.User.models import UserModel
from modules.Ecscursion.models import EcscursionModel


class PassEcscursionModel(BaseModel):
    id: Optional[str] = None

    user: UserModel
    ecscursion: EcscursionModel
    is_finished: bool
    start_time: datetime
    finish_time: Optional[datetime]
    correct_answers: int
    points: int

    @classmethod
    def get_collection_name(cls) -> str:
        return "pass_ecscursion"

    def to_json(self, with_ids=False):
        data: Dict[str, Any]
        data = {
            "user": self.user.to_json() if not with_ids else self.user.id,
            "ecscursion": self.ecscursion.to_json() if not with_ids else self.user.id,
            "is_finished": self.is_finished,
            "start_time": str(self.start_time),
            "finish_time": str(self.finish_time),
            "correct_answers": int,
            "points": int,
        }

        return data

    @classmethod
    async def document_to_object(cls, document) -> 'PassEcscursionModel':
        document['id'] = str(document['_id'])
        document.pop('_id')
        document['user'] = await UserModel.get(id=document['user'])
        document['ecscursion'] = await EcscursionModel.get(id=document['ecscursion'])
        return cls(**document)

    @classmethod
    async def get(cls, **kwargs) -> Optional['PassEcscursionModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        document = await db.db[cls.get_collection_name()].find_one(kwargs)
        if document:
            return await cls.document_to_object(document)
        return None

    @classmethod
    async def find(cls, **kwargs) -> List['PassEcscursionModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        cursor = db.db[cls.get_collection_name()].find(kwargs)
        pass_ecscursions = []
        async for document in cursor:
            pass_ecscursions.append(await cls.document_to_object(document))
        return pass_ecscursions

    async def create(self):
        new_document = self.to_json(with_ids=True)
        result = await db.db[self.get_collection_name()].insert_one(new_document)
        self.id = str(result.inserted_id)

    async def update(self):
        document = self.to_json(with_ids=True)
        document.pop('id')
        await db.db[self.get_collection_name()].update_one(
            {'_id': ObjectId(self.id)}, {'$set': document})

    async def delete(self):
        await db.db[self.get_collection_name()].delete_one(
            {'_id': ObjectId(self.id)})
