from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any, Union
from datetime import datetime
from bson import ObjectId

from db import db

from modules.User.models import UserModel


class QuestionModel(BaseModel):
    id: Optional[str] = None

    title: str
    answers: List[str] = []
    correct_answers: List[str] = []

    @classmethod
    def get_collection_name(cls) -> str:
        return "question"

    def to_json(self, with_ids=False):
        data: Dict[str, Any]
        data = {
            "title": self.title,
            "answers": self.answers,
            "correct_answers": self.correct_answers,
        }

        if self.id:
            data["id"] = self.id

        return data

    @classmethod
    async def document_to_object(cls, document) -> 'QuestionModel':
        document['id'] = str(document['_id'])
        document.pop('_id')

        return cls(**document)

    @classmethod
    async def get(cls, **kwargs) -> Optional['QuestionModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        document = await db.db[cls.get_collection_name()].find_one(kwargs)
        if document:
            return await cls.document_to_object(document)
        return None

    @classmethod
    async def find(cls, **kwargs) -> List['QuestionModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        cursor = db.db[cls.get_collection_name()].find(kwargs)
        questions = []
        async for document in cursor:
            questions.append(await cls.document_to_object(document))
        return questions

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


class EcscursionPartModel(BaseModel):
    id: Optional[str] = None

    title: str
    audio: str
    materials: List[str]
    is_test: bool
    test: List[QuestionModel] = []

    @classmethod
    def get_collection_name(cls) -> str:
        return "ecscursion_part"

    def to_json(self, with_ids=False):
        data: Dict[str, Any]
        data = {
            "title": self.title,
            "audio": self.audio,
            "materials": self.materials,
            "is_test": self.is_test,
        }

        if self.id:
            data['id'] = self.id

        test = []
        if with_ids:
            for q in self.test:
                test.append(q.id)
        else:
            for q in self.test:
                test.append(q.to_json())

        data['test'] = test

        return data

    @classmethod
    async def document_to_object(cls, document) -> 'EcscursionPartModel':
        document['id'] = str(document['_id'])
        document.pop('_id')
        test = []
        for q in document['test']:
            test.append(await QuestionModel.get(id=q))
        document['test'] = test
        return cls(**document)

    @classmethod
    async def get(cls, **kwargs) -> Optional['EcscursionPartModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        document = await db.db[cls.get_collection_name()].find_one(kwargs)
        if document:
            return await cls.document_to_object(document)
        return None

    @classmethod
    async def find(cls, **kwargs) -> List['EcscursionPartModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        cursor = db.db[cls.get_collection_name()].find(kwargs)
        ecscursion_parts = []
        async for document in cursor:
            ecscursion_parts.append(await cls.document_to_object(document))
        return ecscursion_parts

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


class EcscursionModel(BaseModel):
    id: Optional[str] = None

    author: UserModel
    title: str
    description: str
    preview_img: str
    need_time: int
    distance: int
    route_url: str
    parts: List[EcscursionPartModel]

    @classmethod
    def get_collection_name(cls) -> str:
        return "ecscursion"

    def to_json(self, with_ids=False):
        data: Dict[str, Any]
        data = {
            "title": self.title,
            "description": self.description,
            "preview_img": self.preview_img,
            "need_time": self.need_time,
            "distance": self.distance,
            "route_url": self.route_url,
        }

        if self.id:
            data['id'] = self.id

        parts = []
        if with_ids:
            for part in self.parts:
                parts.append(part.id)
            data['author'] = self.author.id
        else:
            for part in self.parts:
                parts.append(part.to_json())
            data['author'] = self.author.to_json()

        data['parts'] = parts

        return data

    @classmethod
    async def document_to_object(cls, document) -> 'EcscursionModel':
        document['id'] = str(document['_id'])
        document.pop('_id')
        parts = []
        for part in document['parts']:
            parts.append(await QuestionModel.get(id=part))
        document['parts'] = parts
        document['author'] = UserModel.get(id=document['author'])
        return cls(**document)

    @classmethod
    async def get(cls, **kwargs) -> Optional['EcscursionModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        document = await db.db[cls.get_collection_name()].find_one(kwargs)
        if document:
            return await cls.document_to_object(document)
        return None

    @classmethod
    async def find(cls, **kwargs) -> List['EcscursionModel']:
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        cursor = db.db[cls.get_collection_name()].find(kwargs)
        ecscursions = []
        async for document in cursor:
            ecscursions.append(await cls.document_to_object(document))
        return ecscursions

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
