import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

url_object = URL.create(
    "oracle+oracledb",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    query={"service_name": os.getenv("DB_SERVICE")}
)

engine = create_engine(url_object)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()