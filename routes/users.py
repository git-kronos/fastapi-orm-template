from typing import List

from fastapi import APIRouter

from models import User
from .schemas import UserSchemaOUT, UserSchemaIn

route = APIRouter(tags=['auth'], prefix='/auth')


@route.post('/', response_model=UserSchemaOUT)
def create_user(data: UserSchemaIn):
    obj = User.objects.create(payload=data.dict())
    return obj


@route.get('/all', response_model=List[UserSchemaOUT])
def all_user():
    obj = User.objects.all()
    return obj
