import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

CLIENTS_SERVICE_DEV_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME")
)

pg_engine = create_engine(CLIENTS_SERVICE_DEV_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=pg_engine)
session = Session()
