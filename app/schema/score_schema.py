from pydantic import BaseModel


class ScoreSubmitSchema(BaseModel):
    game_slug: str
    player: str
    score: int


class ScoreResponseSchema(BaseModel):
    id: int
    game_slug: str
    player: str
    score: int

    class Config:
        from_attributes = True
