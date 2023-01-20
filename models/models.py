from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.database import *


class Blog(Base):
    __tablename__ = "Blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    published = Column(Boolean)
    
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    