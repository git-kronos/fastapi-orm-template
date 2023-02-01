import sqlalchemy as sa

from utils import Manager
from utils.envs import Base


class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    email = sa.Column(sa.String(100), unique=True, index=True)
    password = sa.Column(sa.String(255), nullable=False)

    objects = Manager()

    def __repr__(self):
        return f"{self.__class__.__name__}: <id={self.id}>"
