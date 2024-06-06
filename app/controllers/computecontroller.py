from sqlalchemy.orm import Session
from app.helpers.computehelper import calculate
from app.models.computemodel import Compute
from app.schemas.computeschema import ComputeRequest, ComputeResponse, Response
import datetime
from fastapi import HTTPException
from app.helpers.logger import logger

def create(db: Session, data: ComputeResponse):
    try:
        start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = calculate(data.payload)
        end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        logger.error(f"Unable to Compute {str(e)}")

    try:
        db_entry = Compute(
            batch_id=data.batch_id,
            input=str(data.payload),
            output=str(output)
        )
        db.add(db_entry)
        db.commit()
        db.refresh(db_entry)
    except Exception as e:
        logger.error(f"Unable to add db entry {str(e)}")
        return {
            'batch_id': data.batch_id,
            'response': [],
            'status': "failed",
            "started_at": start,
            "completed_at": ""
        }
    return {
        'batch_id': data.batch_id,
        'response': output,
        'status': "complete",
        "started_at": start,
        "completed_at": end
    }

def get_result(db: Session, batch_id: int):
    result = None
    try:
        result = db.query(Compute).filter(Compute.batch_id == batch_id).first()
        if result is not None:
            raise HTTPException(status_code=404,detail="Batch ID not found")
    except Exception as e:
        result = {"message": "Batch ID not Found"}
    return result

def get_results(db: Session, skip: int = 0, limit: int = 100):
    results = None
    try:
        results = db.query(Compute).offset(skip).limit(limit).all()
        if results is not None:
            raise HTTPException(status_code=404,detail="No Data found")
    except Exception as e:
        results = {"message": "No Data"}
    return results
    
