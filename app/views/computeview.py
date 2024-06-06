import logging
from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.models.computemodel import *
from app.schemas.computeschema import ComputeResponse, ComputeRequest, Response
from app.controllers.computecontroller import create, get_result, get_results 
from app.db.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/compute/', response_model=ComputeResponse)
def compute(request: ComputeRequest, db: Session = Depends(get_db)):
    return create(db=db, data=request)

@router.get('/compute/', response_model=List[Response])
def computed_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = get_results(db, skip=skip, limit=limit)
    return results

@router.get('/compute/{id}', response_model=Response)
def computed_result_by_id(id: str, db: Session = Depends(get_db)):
    result = get_result(db, batch_id=id)
    if not result:
        raise HTTPException(status_code=404, detail="Batch ID not found.")
    return result    
