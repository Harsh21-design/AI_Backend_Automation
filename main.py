from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):

    title: str
    description: str
    completed: bool = False

@app.get("/")
def home():
    return {"message":"Day 1 Backend Journey started"}

@app.get("/health")
def health():
    return {"status":"OK"}


@app.post("/task")
def create_task(task: Task):
    return {
        "message":"new task created successfully",
        "task": task
    }

