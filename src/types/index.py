from pydantic import BaseModel
from typing import List, Dict

class BotResponse(BaseModel):
    bot_name: str
    response: str

class VotingResult(BaseModel):
    bot_name: str
    votes: int

class Summary(BaseModel):
    responses: Dict[str, List[BotResponse]]
    voting_results: List[VotingResult]
    best_bot: str
    total_votes: int

class Query(BaseModel):
    query_text: str
    bot_names: List[str]
