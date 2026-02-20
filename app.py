from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import models
app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result=numbers.num1+numbers.num2
    return {"result": result}

user1 = models.User(name="Зырянова Арина", id=1)

@app.get("/users")
async def user_info():
    return user1

@app.post("/user")
async def check_user(user2: models.UserAge):
    is_adult=user2.age>=18
    return {"name": user2.name,
             "age": user2.age, 
            "is_adult": is_adult}

comments=[]
@app.post("/feedback")
async def feedback(fb:models.Feedback):
    comments.append(fb)
    return {"message": f"Feedback received. Thank you, {fb.name}"}

comments2=[]
@app.post("/feedback2")
async def feedback2(fb:models.Feedback2):
    comments.append(fb)
    return {"message":f"Спасибо,{fb.name}! Ваш отзыв сохранён."}