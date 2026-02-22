from typing import List
from app.models import Score


class ScoreRepository:
    @staticmethod
    async def upsert(game_slug: str, player: str, score: int) -> Score:
        obj, created = await Score.get_or_create(
            game_slug=game_slug, player=player,
            defaults={"score": score}
        )
        if not created:
            obj.score = score
            await obj.save()
        return obj

    @staticmethod
    async def get_by_game_slug(game_slug: str) -> List[Score]:
        return await Score.filter(game_slug=game_slug).order_by("-score")
