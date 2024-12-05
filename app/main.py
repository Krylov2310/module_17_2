from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from routers import task, user

app = FastAPI()
info_ed = ('<h2>Домашнее задание по теме "Модели SQLALchemy.<br>'
           'Отношения между таблицами."</h2>'
           '<h3>Цель: усвоить основные правила структурирования проекта с использованием FastAPI.'
           '<br>Научиться создавать модели баз данных, используя SQLAlchemy.'
           '<br>Студент Крылов Эдуард Васильевич'
           '<br>Дата: 05.12.2024г.</h3>')


# python -m uvicorn main:app
# Get
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


@app.get("/info", response_class=HTMLResponse)
async def info():
    return info_ed


app.include_router(task.router)
app.include_router(user.router)
# python -m uvicorn main:app
