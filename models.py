from pydantic import BaseModel
from pydantic import Field, field_validator

class User(BaseModel):
    name: str
    id: int

class UserAge(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name:str
    message:str

class Feedback2(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message:str = Field(..., min_length=10, max_length=500)
    @field_validator('message')
    @classmethod
    def check_message(cls, v: str) -> str:
        stop_words=["кринж", "рофл", "вайб"]
        check_mes=v.lower()
        for i in stop_words:
            if i in check_mes:
                raise ValueError("Использование недопустимых слов")
            
        return v
