import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite://./db.sqlite3"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000

    # S3 Configuration
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    aws_region: str = "us-east-1"
    s3_bucket_name: str = "mandarin-learning-files"

    class Config:
        env_file = ".env"


settings = Settings()
