from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.database import *


class Blog(Base):
    __tablename__ = "Blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    published = Column(Boolean)
    