import logging
from typing import List
import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schema
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# setup loggers
logging.config.fileConfig('app/logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/compute/', response_model=schema.ComputeResponse)
def compute(request: schema.ComputeRequest, db: Session = Depends(get_db)):
    return crud.compute(db=db, data=request)

@app.get('/compute/', response_model=List[schema.Response])
def computed_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = crud.get_results(db, skip=skip, limit=limit)
    return results


@app.get('/compute/{id}', response_model=schema.Response)
def computed_result_by_id(id: str, db: Session = Depends(get_db)):
    result = crud.get_result(db, batch_id=id)

    if not result:
        raise HTTPException(status_code=404, detail="Batch ID not found.")
    return result    


