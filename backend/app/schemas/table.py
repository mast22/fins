from pydantic import BaseModel
from typing import Optional, List


class Saving(BaseModel):
    id: int
    amount: float


class TablePost(BaseModel):
    columns: List
    savings: List[Saving]
