from pydantic import BaseModel
from typing import Optional


class CategoryCreateSchema(BaseModel):
    name: str
    hsk_level: int


class CategoryUpdateSchema(BaseModel):
    name: Optional[str] = None
    hsk_level: Optional[int] = None


class CategoryResponseSchema(BaseModel):
    id: int
    name: str
    hsk_level: int

    class Config:
        from_attributes = True
