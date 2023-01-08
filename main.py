from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"data":"about page"}


@app.get("/blogs")
def blog():
    return {"data": ["blog1", "blog2", "blog3"]}


@app.get("/blog/{id}")
def blog(id):
    return {"data":{"blog_id": id}}

