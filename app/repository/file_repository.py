from typing import List, Optional
from app.models import File


class FileRepository:
    @staticmethod
    async def create(name: str, bucket: str) -> File:
        return await File.create(name=name, bucket=bucket)

    @staticmethod
    async def get_by_id(file_id: int) -> Optional[File]:
        return await File.get_or_none(id=file_id)

    @staticmethod
    async def delete(file_id: int) -> bool:
        file = await File.get_or_none(id=file_id)
        if file:
            await file.delete()
            return True
        return False
