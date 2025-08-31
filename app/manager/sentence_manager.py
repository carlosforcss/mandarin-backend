from typing import List, Optional
from app.repository.sentence_repository import SentenceRepository
from app.repository.models import Sentence
from app.schema.sentence_schema import SentenceCreateSchema, SentenceUpdateSchema


class SentenceManager:
    def __init__(self):
        self.repository = SentenceRepository()

    async def create_sentence(self, sentence_data: SentenceCreateSchema) -> Sentence:
        return await self.repository.create(
            sentence_text=sentence_data.sentence_text,
            pinyin=sentence_data.pinyin,
            meaning=sentence_data.meaning,
            category_id=sentence_data.category_id,
            hanzi_ids=sentence_data.hanzi_ids,
        )

    async def get_sentence(self, sentence_id: int) -> Optional[Sentence]:
        return await self.repository.get_by_id(sentence_id)

    async def get_all_sentences(
        self, skip: int = 0, limit: int = 100
    ) -> List[Sentence]:
        return await self.repository.get_all(skip=skip, limit=limit)

    async def get_sentences_by_category(
        self, category_id: int, skip: int = 0, limit: int = 100
    ) -> List[Sentence]:
        return await self.repository.get_by_category(
            category_id, skip=skip, limit=limit
        )

    async def update_sentence(
        self, sentence_id: int, sentence_data: SentenceUpdateSchema
    ) -> Optional[Sentence]:
        update_data = sentence_data.dict(exclude_unset=True)
        return await self.repository.update(sentence_id, **update_data)

    async def delete_sentence(self, sentence_id: int) -> bool:
        return await self.repository.delete(sentence_id)
