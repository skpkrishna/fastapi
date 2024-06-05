import logging
from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app import models, schemas, controllers
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# get root logger
logger = logging.getLogger(__name__)
router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/compute/', response_model=schemas.ComputeResponse)
def compute(request: schemas.ComputeRequest, db: Session = Depends(get_db)):
    return controllers.create(db=db, data=request)

@router.get('/compute/', response_model=List[schemas.Response])
def computed_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = controllers.get_results(db, skip=skip, limit=limit)
    return results

@router.get('/compute/{id}', response_model=schemas.Response)
def computed_result_by_id(id: str, db: Session = Depends(get_db)):
    result = controllers.get_result(db, batch_id=id)
    if not result:
        raise HTTPException(status_code=404, detail="Batch ID not found.")
    return result    
