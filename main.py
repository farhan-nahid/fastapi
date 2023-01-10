from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from database.database import *
from models import models
from schemas.schemas import Blog

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"data":"about page"}


@app.get("/blogs")
def blog(limit:Optional[int] = 10, published:Optional[bool] = True, sort: Optional[str] = None):
    return {"data": ["blog1", "blog2", "blog3"], "limit":limit, "published":published, "sort":sort}




# connection to database

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def add_blog(blog : Blog, db: Session= Depends(get_db)):
    new_blog = models.Blog(title=blog.title, description=blog.description, published=blog.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
   

@app.get("/blog", status_code=status.HTTP_200_OK)
def get_blog(db: Session= Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_blog_by_id(id:int, db: Session= Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    else :
        return blog