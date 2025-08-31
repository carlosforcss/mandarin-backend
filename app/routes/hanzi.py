from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.manager.hanzi_manager import HanziManager
from app.schema.hanzi_schema import HanziSchema, HanziCreateSchema, HanziUpdateSchema

router = APIRouter()
hanzi_manager = HanziManager()


@router.post("/", response_model=HanziSchema)
async def create_hanzi(hanzi_data: HanziCreateSchema):
    return await hanzi_manager.create_hanzi(hanzi_data)


@router.get("/{hanzi_id}", response_model=HanziSchema)
async def get_hanzi(hanzi_id: int):
    hanzi = await hanzi_manager.get_hanzi(hanzi_id)
    if not hanzi:
        raise HTTPException(status_code=404, detail="Hanzi not found")
    return hanzi


@router.get("/", response_model=List[HanziSchema])
async def get_all_hanzis(skip: int = 0, limit: int = 100):
    return await hanzi_manager.get_all_hanzis(skip=skip, limit=limit)


@router.get("/hsk/{hsk_level}", response_model=List[HanziSchema])
async def get_hanzis_by_hsk_level(hsk_level: int, skip: int = 0, limit: int = 100):
    return await hanzi_manager.get_hanzis_by_hsk_level(
        hsk_level, skip=skip, limit=limit
    )


@router.get("/category/{category_id}", response_model=List[HanziSchema])
async def get_hanzis_by_category(
    category_id: int,
    hsk_level: Optional[int] = Query(None),
    skip: int = 0,
    limit: int = 100,
):
    return await hanzi_manager.get_hanzis_by_category_and_hsk_level(
        category_id, hsk_level, skip=skip, limit=limit
    )


@router.put("/{hanzi_id}", response_model=HanziSchema)
async def update_hanzi(hanzi_id: int, hanzi_data: HanziUpdateSchema):
    hanzi = await hanzi_manager.update_hanzi(hanzi_id, hanzi_data)
    if not hanzi:
        raise HTTPException(status_code=404, detail="Hanzi not found")
    return hanzi


@router.delete("/{hanzi_id}")
async def delete_hanzi(hanzi_id: int):
    deleted = await hanzi_manager.delete_hanzi(hanzi_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Hanzi not found")
    return {"message": "Hanzi deleted successfully"}
