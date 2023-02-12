import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
DATABASE = os.environ.get("DB")
USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("DB_PASSWORD")
CONNECTION_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
ENGINE = create_engine(CONNECTION_URL)
SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BASE = declarative_base()
