from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, validator

app = FastAPI(title="Hello API with Validation")

class UserSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Name must be 2-50 characters")
    email: EmailStr
    contact: str = Field(..., description="10-digit mobile number")

    @validator("contact")
    def validate_contact(cls, v):
        if not v.isdigit():
            raise ValueError("Contact must contain only digits")
        if len(v) != 10:
            raise ValueError("Contact must be exactly 10 digits")
        return v

    class Config:
        orm_mode = True


@app.get("/")
def home():
    return {"message": "Welcome to Hello API"}

@app.post("/hello")
def say_hello(user: UserSchema):
    return {
        "message": f"Hello {user.name}!",
        "email": user.email,
        "contact": user.contact
    }
