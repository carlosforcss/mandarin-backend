from fastapi import APIRouter, HTTPException
from typing import List
from app.manager.sentence_manager import SentenceManager
from app.schema.sentence_schema import (
    SentenceSchema,
    SentenceCreateSchema,
    SentenceUpdateSchema,
)

router = APIRouter()
sentence_manager = SentenceManager()


@router.post("/", response_model=SentenceSchema)
async def create_sentence(sentence_data: SentenceCreateSchema):
    return await sentence_manager.create_sentence(sentence_data)


@router.get("/{sentence_id}", response_model=SentenceSchema)
async def get_sentence(sentence_id: int):
    sentence = await sentence_manager.get_sentence(sentence_id)
    if not sentence:
        raise HTTPException(status_code=404, detail="Sentence not found")
    return sentence


@router.get("/", response_model=List[SentenceSchema])
async def get_all_sentences(skip: int = 0, limit: int = 100):
    return await sentence_manager.get_all_sentences(skip=skip, limit=limit)


@router.get("/category/{category_id}", response_model=List[SentenceSchema])
async def get_sentences_by_category(category_id: int, skip: int = 0, limit: int = 100):
    return await sentence_manager.get_sentences_by_category(
        category_id, skip=skip, limit=limit
    )


@router.put("/{sentence_id}", response_model=SentenceSchema)
async def update_sentence(sentence_id: int, sentence_data: SentenceUpdateSchema):
    sentence = await sentence_manager.update_sentence(sentence_id, sentence_data)
    if not sentence:
        raise HTTPException(status_code=404, detail="Sentence not found")
    return sentence


@router.delete("/{sentence_id}")
async def delete_sentence(sentence_id: int):
    deleted = await sentence_manager.delete_sentence(sentence_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sentence not found")
    return {"message": "Sentence deleted successfully"}
