from typing import List, Optional
from app.repository.category_repository import CategoryRepository
from app.repository.models import Category
from app.schema.category_schema import CategoryCreateSchema, CategoryUpdateSchema


class CategoryManager:
    def __init__(self):
        self.repository = CategoryRepository()

    async def create_category(self, category_data: CategoryCreateSchema) -> Category:
        return await self.repository.create(
            name=category_data.name, hsk_level=category_data.hsk_level
        )

    async def get_category(self, category_id: int) -> Optional[Category]:
        return await self.repository.get_by_id(category_id)

    async def get_all_categories(
        self, skip: int = 0, limit: int = 100
    ) -> List[Category]:
        return await self.repository.get_all(skip=skip, limit=limit)

    async def get_categories_by_hsk_level(self, hsk_level: int) -> List[Category]:
        return await self.repository.get_by_hsk_level(hsk_level)

    async def update_category(
        self, category_id: int, category_data: CategoryUpdateSchema
    ) -> Optional[Category]:
        update_data = category_data.dict(exclude_unset=True)
        return await self.repository.update(category_id, **update_data)

    async def delete_category(self, category_id: int) -> bool:
        return await self.repository.delete(category_id)
