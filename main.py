from fastapi import FastAPI
from fastapi.testclient import TestClient

from routes.users import route as user_routes

app = FastAPI()
client = TestClient(app=app)


@app.get('/')
def root():
    return {}


app.include_router(user_routes, prefix='/api')
