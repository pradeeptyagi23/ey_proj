# models.py
from pydantic import BaseModel
from typing import List
from datetime import datetime

# Pydantic model for request validation
class AdditionRequest(BaseModel):
    batchid: str
    payload: List[List[int]]

# Pydantic model for response validation
class AdditionResponse(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: datetime
    completed_at: datetime
