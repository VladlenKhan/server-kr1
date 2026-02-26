from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from pydantic import BaseModel  
from models import User, UserInput, Feedback

app = FastAPI(title="Контрольная работа №1 — FastAPI")

# Задание 1.2 — корневой маршрут возвращает HTML
@app.get("/")
async def root():
    return FileResponse(Path("index.html"))


# Задание 1.3* — POST /calculate
class Calculate(BaseModel):
    num1: int
    num2: int

@app.post("/calculate")
async def calculate(data: Calculate):
    return {"result": data.num1 + data.num2}


# Задание 1.4 — GET /users
static_user = User(name="Хан Владлен", id=1)   

@app.get("/users")
async def get_user():
    return static_user


# Задание 1.5* — POST /user + is_adult
@app.post("/user")
async def create_user(user: UserInput):
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.age >= 18
    }


# Задания 2.1 + 2.2* — POST /feedback с валидацией
feedbacks: list[Feedback] = []

@app.post("/feedback")
async def post_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}