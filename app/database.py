from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://<postgres>:<Ugonaza818>@localhost/<fastapp>"
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'
# engine = create_engine("postgresql://postgres:Ugonaza818@localhost/fastapi", pool_pre_ping=True)
# engine = create_engine("postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}", pool_pre_ping=True)
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
engine.connect()

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# function responsible to talking to our database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Setting up our connection to database
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Ugonaza818', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection successful")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error: ", error)
#         time.sleep(2)
