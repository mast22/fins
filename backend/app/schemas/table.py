from pydantic import BaseModel
from typing import Optional, List


class Saving(BaseModel):
    id: int
    amount: float


class TablePost(BaseModel):
    savings_sets: List
    savings: List[Saving]
