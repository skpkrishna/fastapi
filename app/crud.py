from sqlalchemy.orm import Session
from . import models, schema, helper
import datetime, logging

# setup loggers
# logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)


def compute(db: Session, data: schema.ComputeResponse):
    try:
        start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = helper.calculate(data.payload)
        end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        logger.error(f"Unable to Compute {str(e)}")

    try:
        db_entry = models.Compute(
            id=data.batchid,
            input=str(data.payload),
            output=str(output)
        )
        db.add(db_entry)
        db.commit()
        db.refresh(db_entry)
    except Exception as e:
        logger.error(f"Unable to add db entry {str(e)}")
        return {
            'batchid': data.batchid,
            'response': [],
            'status': "failed",
            "started_at": start,
            "completed_at": ""
        }
    return {
        'batchid': data.batchid,
        'response': output,
        'status': "complete",
        "started_at": start,
        "completed_at": end
    }

def get_result(db: Session, batch_id: int):
    return db.query(models.Compute).filter(models.Compute.id == batch_id).first()

def get_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Compute).offset(skip).limit(limit).all()