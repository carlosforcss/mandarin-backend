import boto3
from botocore.exceptions import ClientError
from typing import Optional
from app.config.settings import settings


class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region,
        )
        self.bucket_name = settings.s3_bucket_name

    async def upload_file(
        self,
        file_content: bytes,
        file_name: str,
        content_type: str = "application/octet-stream",
    ) -> bool:
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=file_content,
                ContentType=content_type,
            )
            return True
        except ClientError:
            return False

    async def delete_file(self, file_name: str) -> bool:
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_name)
            return True
        except ClientError:
            return False

    async def get_file_url(
        self, file_name: str, expiration: int = 3600
    ) -> Optional[str]:
        try:
            url = self.s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": self.bucket_name, "Key": file_name},
                ExpiresIn=expiration,
            )
            return url
        except ClientError:
            return None

    async def file_exists(self, file_name: str) -> bool:
        try:
            self.s3_client.head_object(Bucket=self.bucket_name, Key=file_name)
            return True
        except ClientError:
            return False

    async def download_file(self, file_name: str) -> Optional[bytes]:
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_name)
            return response["Body"].read()
        except ClientError:
            return None
