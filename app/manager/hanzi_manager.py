from typing import List, Optional
from app.repository.hanzi_repository import HanziRepository
from app.models import Hanzi
from app.schema.hanzi_schema import HanziCreateSchema, HanziUpdateSchema


class HanziManager:
    def __init__(self):
        self.repository = HanziRepository()

    async def create_hanzi(self, hanzi_data: HanziCreateSchema) -> Hanzi:
        return await self.repository.create(
            hanzi_text=hanzi_data.hanzi_text,
            pinyin=hanzi_data.pinyin,
            meaning=hanzi_data.meaning,
            hsk_level=hanzi_data.hsk_level,
            image_file_id=hanzi_data.image_file_id,
            category_id=hanzi_data.category_id,
        )

    async def get_hanzi(self, hanzi_id: int) -> Optional[Hanzi]:
        return await self.repository.get_by_id(hanzi_id)

    async def get_all_hanzis(self, skip: int = 0, limit: int = 100) -> List[Hanzi]:
        return await self.repository.get_all(skip=skip, limit=limit)

    async def get_hanzis_by_hsk_level(
        self, hsk_level: int, skip: int = 0, limit: int = 100
    ) -> List[Hanzi]:
        return await self.repository.get_by_hsk_level(hsk_level, skip=skip, limit=limit)

    async def get_hanzis_by_category_and_hsk_level(
        self,
        category_id: int,
        hsk_level: Optional[int] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Hanzi]:
        return await self.repository.get_by_category_and_hsk_level(
            category_id, hsk_level, skip=skip, limit=limit
        )

    async def update_hanzi(
        self, hanzi_id: int, hanzi_data: HanziUpdateSchema
    ) -> Optional[Hanzi]:
        update_data = hanzi_data.dict(exclude_unset=True)
        return await self.repository.update(hanzi_id, **update_data)

    async def delete_hanzi(self, hanzi_id: int) -> bool:
        return await self.repository.delete(hanzi_id)
