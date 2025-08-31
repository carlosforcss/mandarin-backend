from typing import List, Optional
from app.repository.models import Sentence


class SentenceRepository:
    @staticmethod
    async def create(
        sentence_text: str,
        pinyin: str,
        meaning: str,
        category_id: Optional[int] = None,
        hanzi_ids: Optional[List[int]] = None,
    ) -> Sentence:
        sentence = await Sentence.create(
            sentence_text=sentence_text,
            pinyin=pinyin,
            meaning=meaning,
            category_id=category_id,
        )
        if hanzi_ids:
            await sentence.hanzis.add(*hanzi_ids)
        return sentence

    @staticmethod
    async def get_by_id(sentence_id: int) -> Optional[Sentence]:
        return await Sentence.get_or_none(id=sentence_id).prefetch_related(
            "category", "hanzis"
        )

    @staticmethod
    async def get_all(skip: int = 0, limit: int = 100) -> List[Sentence]:
        return (
            await Sentence.all()
            .offset(skip)
            .limit(limit)
            .prefetch_related("category", "hanzis")
        )

    @staticmethod
    async def get_by_category(
        category_id: int, skip: int = 0, limit: int = 100
    ) -> List[Sentence]:
        return (
            await Sentence.filter(category_id=category_id)
            .offset(skip)
            .limit(limit)
            .prefetch_related("category", "hanzis")
        )

    @staticmethod
    async def update(sentence_id: int, **kwargs) -> Optional[Sentence]:
        sentence = await Sentence.get_or_none(id=sentence_id)
        if sentence:
            hanzi_ids = kwargs.pop("hanzi_ids", None)
            await sentence.update_from_dict(kwargs)
            await sentence.save()
            if hanzi_ids is not None:
                await sentence.hanzis.clear()
                if hanzi_ids:
                    await sentence.hanzis.add(*hanzi_ids)
            return sentence
        return None

    @staticmethod
    async def delete(sentence_id: int) -> bool:
        sentence = await Sentence.get_or_none(id=sentence_id)
        if sentence:
            await sentence.delete()
            return True
        return False
