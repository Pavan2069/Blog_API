from fastapi import FastAPI
from database import engine
import models

#Creating tables in the database
models.Base.metadata.create_all(bind=engine)
   
app=FastAPI()

@app.get("/")
def home():
    return {
        "message":"Blog API Started"
    }
