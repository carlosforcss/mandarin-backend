from pydantic import BaseModel
from typing import Optional, List
from app.schema.hanzi_schema import HanziSchema
from app.schema.category_schema import CategoryResponseSchema


class SentenceSchema(BaseModel):
    id: int
    sentence_text: str
    pinyin: str
    meaning: str
    category: Optional[CategoryResponseSchema] = None
    hanzis: List[HanziSchema] = []

    class Config:
        from_attributes = True


class SentenceCreateSchema(BaseModel):
    sentence_text: str
    pinyin: str
    meaning: str
    category_id: Optional[int] = None
    hanzi_ids: Optional[List[int]] = []


class SentenceUpdateSchema(BaseModel):
    sentence_text: Optional[str] = None
    pinyin: Optional[str] = None
    meaning: Optional[str] = None
    category_id: Optional[int] = None
    hanzi_ids: Optional[List[int]] = None
