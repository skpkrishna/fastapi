from pydantic import BaseModel
from datetime import datetime

class ComputeRequest(BaseModel):
    batch_id: str
    payload: list

class ComputeResponse(BaseModel):
    batch_id: str
    response: list
    status: str
    started_at: str
    completed_at: str

class Response(BaseModel):
    batch_id: str
    input: str
    output: str
    started_at: datetime = None

