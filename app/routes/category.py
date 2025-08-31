from fastapi import APIRouter, HTTPException
from typing import List
from app.manager.category_manager import CategoryManager
from app.schema.category_schema import (
    CategoryResponseSchema,
    CategoryCreateSchema,
    CategoryUpdateSchema,
)

router = APIRouter()
category_manager = CategoryManager()


@router.post("/", response_model=CategoryResponseSchema)
async def create_category(category_data: CategoryCreateSchema):
    return await category_manager.create_category(category_data)


@router.get("/{category_id}", response_model=CategoryResponseSchema)
async def get_category(category_id: int):
    category = await category_manager.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/", response_model=List[CategoryResponseSchema])
async def get_all_categories(skip: int = 0, limit: int = 100):
    return await category_manager.get_all_categories(skip=skip, limit=limit)


@router.get("/hsk/{hsk_level}", response_model=List[CategoryResponseSchema])
async def get_categories_by_hsk_level(hsk_level: int):
    return await category_manager.get_categories_by_hsk_level(hsk_level)


@router.put("/{category_id}", response_model=CategoryResponseSchema)
async def update_category(category_id: int, category_data: CategoryUpdateSchema):
    category = await category_manager.update_category(category_id, category_data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{category_id}")
async def delete_category(category_id: int):
    deleted = await category_manager.delete_category(category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}
