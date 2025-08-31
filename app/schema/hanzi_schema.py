from pydantic import BaseModel
from typing import Optional


class FileSchema(BaseModel):
    id: int
    name: str
    bucket: str

    class Config:
        from_attributes = True


class CategorySchema(BaseModel):
    id: int
    name: str
    hsk_level: int

    class Config:
        from_attributes = True


class HanziSchema(BaseModel):
    id: int
    hanzi_text: str
    pinyin: str
    meaning: str
    hsk_level: int
    image_file_id: Optional[int] = None
    category_id: Optional[int] = None

    class Config:
        from_attributes = True


class HanziCreateSchema(BaseModel):
    hanzi_text: str
    pinyin: str
    meaning: str
    hsk_level: int
    image_file_id: Optional[int] = None
    category_id: Optional[int] = None


class HanziUpdateSchema(BaseModel):
    hanzi_text: Optional[str] = None
    pinyin: Optional[str] = None
    meaning: Optional[str] = None
    hsk_level: Optional[int] = None
    image_file_id: Optional[int] = None
    category_id: Optional[int] = None
