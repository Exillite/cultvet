from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any, Union
from bson import ObjectId

from db import db


class UserModel(BaseModel):
    id: Optional[str] = None

    tg_id: int
    points: int = 0

    @classmethod
    def get_collection_name(cls) -> str:
        return "user"

    def to_json(self, with_ids=False):
        data: Dict[str, Any]
        data = {
            "tg_id": self.tg_id,
            "points": self.points,
        }

        if self.id:
            data["id"] = self.id

        return data

    @classmethod
    async def document_to_object(cls, document) -> 'UserModel':
        document['id'] = str(document['_id'])
        document.pop('_id')

        return cls(**document)

    @classmethod
    async def get(cls, **kwargs) -> Optional['UserModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        document = await db.db[cls.get_collection_name()].find_one(kwargs)
        if document:
            return await cls.document_to_object(document)
        return None

    @classmethod
    async def find(cls, **kwargs) -> List['UserModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        cursor = db.db[cls.get_collection_name()].find(kwargs)
        users = []
        async for document in cursor:
            users.append(await cls.document_to_object(document))
        return users

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
