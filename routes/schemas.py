from pydantic import BaseModel, EmailStr, validator

from utils import hash_password


class UserSchemaIn(BaseModel):
    email: EmailStr
    password: str

    @validator('password')
    def validate_password(cls, value):
        return hash_password(value)


class UserSchemaOUT(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
