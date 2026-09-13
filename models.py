from sqlalchemy import Column,Integer,String,Text
from Blog_API.database import Base

#Blog Table
class Blog(Base): #Make Blog an SQL Alchemy model by inheriting from Base
    __tablename__="blogs"

    id = Column(Integer,primary_key=True,index=True)
    title=Column(String)
    content=Column(Text)
