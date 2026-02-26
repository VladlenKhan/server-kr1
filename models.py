from pydantic import BaseModel, Field, field_validator


class User(BaseModel):          # Задание 1.4
    name: str
    id: int


class UserInput(BaseModel):     # Задание 1.5*
    name: str
    age: int


class Feedback(BaseModel):      # Задания 2.1 + 2.2*
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def validate_no_bad_words(cls, v: str) -> str:
        bad_words = ["кринж", "рофл", "вайб"]
        v_lower = v.lower()
        for word in bad_words:
            if word in v_lower:
                raise ValueError("Использование недопустимых слов")
        return v