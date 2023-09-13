import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import dotenv

dotenv.load_dotenv()
PG_SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"

pg_engine = create_engine(PG_SQLALCHEMY_DATABASE_URL)

PgSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=pg_engine)


session = PgSessionLocal()
session.commit = session.flush
