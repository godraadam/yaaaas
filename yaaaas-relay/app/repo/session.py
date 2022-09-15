from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.index import settings

engine = create_engine(settings.DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
