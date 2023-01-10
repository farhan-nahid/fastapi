from typing import Optional

from sqlalchemy.orm import Session

from database.database import *
from fastapi import Depends, FastAPI
from models import models
from schemas.schemas import Blog

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"data":"about page"}

@app.post("/blog")
def add_blog(blog : Blog, db: Session= Depends()):
    return db
    return {"data" : {"title": blog.title, "description": blog.description, "published": blog.published},"message" : "New Blog Created"}


@app.get("/blogs")
def blog(limit:Optional[int] = 10, published:Optional[bool] = True, sort: Optional[str] = None):
    return {"data": ["blog1", "blog2", "blog3"], "limit":limit, "published":published, "sort":sort}


@app.get("/blog/{id}")
def blog(id):
    return {"data":{"blog_id": id}}


