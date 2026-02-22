import boto3
from typing import Optional
from app.config.settings import settings


class PollyService:
    def __init__(self):
        self.client = boto3.client(
            "polly",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region,
        )

    async def synthesize_speech(self, text: str, voice_id: str = "Zhiyu") -> Optional[bytes]:
        try:
            response = self.client.synthesize_speech(
                Text=text,
                OutputFormat="mp3",
                VoiceId=voice_id,
                LanguageCode="cmn-CN"
            )
            
            if "AudioStream" in response:
                return response["AudioStream"].read()
            return None
        except Exception as e:
            print(f"Error synthesizing speech: {e}")
            return None