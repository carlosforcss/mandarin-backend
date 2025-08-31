from typing import List, Optional
from app.repository.models import Category


class CategoryRepository:
    @staticmethod
    async def create(name: str, hsk_level: int) -> Category:
        return await Category.create(name=name, hsk_level=hsk_level)

    @staticmethod
    async def get_by_id(category_id: int) -> Optional[Category]:
        return await Category.get_or_none(id=category_id)

    @staticmethod
    async def get_all(skip: int = 0, limit: int = 100) -> List[Category]:
        return await Category.all().offset(skip).limit(limit)

    @staticmethod
    async def get_by_hsk_level(hsk_level: int) -> List[Category]:
        return await Category.filter(hsk_level=hsk_level)

    @staticmethod
    async def update(category_id: int, **kwargs) -> Optional[Category]:
        category = await Category.get_or_none(id=category_id)
        if category:
            await category.update_from_dict(kwargs)
            await category.save()
            return category
        return None

    @staticmethod
    async def delete(category_id: int) -> bool:
        category = await Category.get_or_none(id=category_id)
        if category:
            await category.delete()
            return True
        return False
