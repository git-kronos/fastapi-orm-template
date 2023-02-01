from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class Envs(BaseSettings):
    db_url: str

    class Config:
        env_file = '.env'


settings = Envs()
engine = create_engine(settings.db_url)
Base = declarative_base()
