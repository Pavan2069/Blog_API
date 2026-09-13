from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="postgresql://postgres:12345@localhost/blogDB"

engine=create_engine(DATABASE_URL)

SesseionLocal=sessionmaker(bind=engine)

Base=declarative_base() # It returns a class