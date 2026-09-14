from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import models,schemas

#Creating tables in the database
models.Base.metadata.create_all(bind=engine)
   
app=FastAPI()

#DB Dependency
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Home
@app.get("/")
def home():
    return {
        "message":"Blog API Started"
    }

#Create Blog
@app.post("/blogs",response_model=schemas.BlogResponse)
def create_blog(blog:schemas.BlogResponse,db:Session=Depends(get_db)):
    new_blog=
