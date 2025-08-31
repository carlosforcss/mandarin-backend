from typing import List, Optional
import uuid
from app.repository.file_repository import FileRepository
from app.repository.models import File
from app.schema.file_schema import FileUpdateSchema
from app.integrations.s3 import S3Service
from app.config.settings import settings


class FileManager:
    def __init__(self):
        self.repository = FileRepository()
        self.s3_service = S3Service()

    async def upload_file(self, file_content: bytes, original_filename: str, content_type: str = "application/octet-stream") -> Optional[File]:
        file_extension = original_filename.split('.')[-1] if '.' in original_filename else ''
        unique_filename = f"{uuid.uuid4()}.{file_extension}" if file_extension else str(uuid.uuid4())
        
        s3_uploaded = await self.s3_service.upload_file(file_content, unique_filename, content_type)
        if not s3_uploaded:
            return None
        
        return await self.repository.create(
            name=unique_filename,
            bucket=settings.s3_bucket_name
        )

    async def get_file(self, file_id: int) -> Optional[File]:
        return await self.repository.get_by_id(file_id)

    async def upload_file_to_s3(
        self,
        file_content: bytes,
        file_name: str,
        content_type: str = "application/octet-stream",
    ) -> bool:
        return await self.s3_service.upload_file(file_content, file_name, content_type)

    async def delete_file(self, file_id: int) -> bool:
        file = await self.repository.get_by_id(file_id)
        if not file:
            return False

        s3_deleted = await self.s3_service.delete_file(file.name)
        if s3_deleted:
            return await self.repository.delete(file_id)
        return False

    async def get_file_url(self, file_id: int, expiration: int = 3600) -> Optional[str]:
        file = await self.repository.get_by_id(file_id)
        if not file:
            return None
        return await self.s3_service.get_file_url(file.name, expiration)

    async def get_file_content(self, file_id: int) -> Optional[bytes]:
        file = await self.repository.get_by_id(file_id)
        if not file:
            return None
        return await self.s3_service.download_file(file.name)
