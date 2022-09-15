import logging
import traceback
from typing import Generator
from fastapi import HTTPException
from app.repo.session import SessionLocal

logger = logging.getLogger(__name__)


def get_db() -> Generator:
    session = SessionLocal()
    try:
        yield session
    except HTTPException as ex:
        logger.error(f"Exception occurred:\n{str(ex.detail)}")
        logger.error(traceback.format_exc())
        session.rollback()
    except Exception as ex:
        logger.error(f"Exception occurred:\n{str(ex)}")
        logger.error(traceback.format_exc())
        session.rollback()
    finally:
        session.close()
