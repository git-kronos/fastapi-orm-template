from fastapi import FastAPI

from routes.users import route as user_routes

app = FastAPI()


@app.get('/')
def root():
    return {}


app.include_router(user_routes, prefix='/api')
