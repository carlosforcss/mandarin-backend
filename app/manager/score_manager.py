from typing import List
from app.models import Score
from app.repository.score_repository import ScoreRepository
from app.schema.score_schema import ScoreSubmitSchema


class ScoreManager:
    def __init__(self):
        self.repository = ScoreRepository()

    async def submit_score(self, data: ScoreSubmitSchema) -> Score:
        return await self.repository.upsert(data.game_slug, data.player, data.score)

    async def get_leaderboard(self, game_slug: str) -> List[Score]:
        return await self.repository.get_by_game_slug(game_slug)
