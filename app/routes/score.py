from typing import List
from fastapi import APIRouter
from app.manager.score_manager import ScoreManager
from app.schema.score_schema import ScoreSubmitSchema, ScoreResponseSchema

router = APIRouter()
score_manager = ScoreManager()


@router.post("/", response_model=ScoreResponseSchema)
async def submit_score(score_data: ScoreSubmitSchema):
    return await score_manager.submit_score(score_data)


@router.get("/{game_slug}", response_model=List[ScoreResponseSchema])
async def get_leaderboard(game_slug: str):
    return await score_manager.get_leaderboard(game_slug)
