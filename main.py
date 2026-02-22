# TASK MANAGEMENT API SYSTEM

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

# empty task list -> all tasks
tasks = []

# create a task
@app.post("/task")
def create_task(task: Task):
    tasks.append(task)
    return {
        "message":"new task created successfully",
        "task": task
    }

# get all task
@app.get("/task")
def get_all_task():
    return {"task:":tasks}


