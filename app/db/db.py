from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Sequence
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.sql import func
from .. import config 
from datetime import datetime

settings = config.get_postgres_settings()
SQLALCHEMY_DATABASE_URL_POSTGRES = f'postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL_POSTGRES)
sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key= True)
    email = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    password = Column(String, nullable=False)
    time_created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    time_updated = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

