from typing import List, Optional
from tortoise.queryset import QuerySet
from app.models import Hanzi


class HanziRepository:
    @staticmethod
    async def create(
        hanzi_text: str,
        pinyin: str,
        meaning: str,
        hsk_level: int,
        image_file_id: Optional[int] = None,
        audio_file_id: Optional[int] = None,
        category_id: Optional[int] = None,
    ) -> Hanzi:
        return await Hanzi.create(
            hanzi_text=hanzi_text,
            pinyin=pinyin,
            meaning=meaning,
            hsk_level=hsk_level,
            image_file_id=image_file_id,
            audio_file_id=audio_file_id,
            category_id=category_id,
        )

    @staticmethod
    async def get_by_id(hanzi_id: int) -> Optional[Hanzi]:
        return await Hanzi.get_or_none(id=hanzi_id)

    @staticmethod
    async def get_all(skip: int = 0, limit: int = 100) -> List[Hanzi]:
        return (
            await Hanzi.all()
            .offset(skip)
            .limit(limit)
        )

    @staticmethod
    async def get_by_hsk_level(
        hsk_level: int, skip: int = 0, limit: int = 100
    ) -> List[Hanzi]:
        return (
            await Hanzi.filter(hsk_level=hsk_level)
            .offset(skip)
            .limit(limit)
        )

    @staticmethod
    async def get_by_category_and_hsk_level(
        category_id: int,
        hsk_level: Optional[int] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Hanzi]:
        query = Hanzi.filter(category_id=category_id)
        if hsk_level is not None:
            query = query.filter(hsk_level=hsk_level)
        return (
            await query.offset(skip)
            .limit(limit)
        )

    @staticmethod
    async def update(hanzi_id: int, **kwargs) -> Optional[Hanzi]:
        hanzi = await Hanzi.get_or_none(id=hanzi_id)
        if hanzi:
            await hanzi.update_from_dict(kwargs)
            await hanzi.save()
            return hanzi
        return None

    @staticmethod
    async def delete(hanzi_id: int) -> bool:
        hanzi = await Hanzi.get_or_none(id=hanzi_id)
        if hanzi:
            await hanzi.delete()
            return True
        return False
