from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import Response
from typing import List
from app.manager.file_manager import FileManager
from app.schema.file_schema import FileResponseSchema

router = APIRouter()
file_manager = FileManager()


@router.post("/upload", response_model=FileResponseSchema)
async def upload_file(file: UploadFile = File(...)):
    file_content = await file.read()
    uploaded_file = await file_manager.upload_file(
        file_content=file_content,
        original_filename=file.filename or "unknown",
        content_type=file.content_type or "application/octet-stream"
    )
    if not uploaded_file:
        raise HTTPException(status_code=500, detail="Failed to upload file")
    return uploaded_file


@router.get("/{file_id}", response_model=FileResponseSchema)
async def get_file(file_id: int):
    file = await file_manager.get_file(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file


@router.get("/{file_id}/content")
async def get_file_content(file_id: int):
    content = await file_manager.get_file_content(file_id)
    if content is None:
        raise HTTPException(status_code=404, detail="File not found")
    return Response(content=content, media_type="application/octet-stream")


@router.delete("/{file_id}")
async def delete_file(file_id: int):
    deleted = await file_manager.delete_file(file_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted successfully"}
