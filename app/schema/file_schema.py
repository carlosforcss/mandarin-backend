from pydantic import BaseModel
from typing import Optional


class FileCreateSchema(BaseModel):
    name: str
    bucket: str


class FileUpdateSchema(BaseModel):
    name: Optional[str] = None
    bucket: Optional[str] = None


class FileResponseSchema(BaseModel):
    id: int
    name: str
    bucket: str

    class Config:
        from_attributes = True
