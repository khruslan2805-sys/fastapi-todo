from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Временное хранилище (вместо базы данных)
tasks = []


# Модель данных
class Task(BaseModel):
    title: str
    description: str


@app.get("/")
def hello():
    return {"message": "Привет! Это TODO API"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Задача добавлена!", "task": task}
