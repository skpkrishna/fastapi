from pydantic import BaseModel
from typing import List, Optional

class ComputeRequest(BaseModel):
    batchid: str
    payload: list

class ComputeResponse(BaseModel):
    batchid: str
    response: list
    status: str
    started_at: str
    completed_at: str

class Response(BaseModel):
    id: str
    input: str
    output: str
    started_at: str = None
