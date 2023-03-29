from dotenv import dotenv_values

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = dotenv_values(".env")

engine = create_engine(config.get('DATABASE_URL'))
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


