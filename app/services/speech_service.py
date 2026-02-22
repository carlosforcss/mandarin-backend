from typing import Optional
import uuid
from app.models import Hanzi, File
from app.integrations.polly import PollyService
from app.integrations.s3 import S3Service
from app.config.settings import settings


class SpeechService:
    def __init__(self):
        self.polly_service = PollyService()
        self.s3_service = S3Service()

    async def get_hanzi_speech(self, hanzi_id: int) -> Optional[bytes]:
        hanzi = await Hanzi.get_or_none(id=hanzi_id).prefetch_related("audio_file")
        if not hanzi:
            return None

        if hanzi.audio_file:
            return await self.s3_service.download_file(hanzi.audio_file.name)

        audio_content = await self.polly_service.synthesize_speech(hanzi.hanzi_text)
        if not audio_content:
            return None

        unique_filename = f"{uuid.uuid4()}.mp3"
        s3_uploaded = await self.s3_service.upload_file(
            audio_content, unique_filename, "audio/mpeg"
        )
        if not s3_uploaded:
            return None

        audio_file = await File.create(
            name=unique_filename,
            bucket=settings.s3_bucket_name
        )
        
        hanzi.audio_file = audio_file
        await hanzi.save()

        return audio_content