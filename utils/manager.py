from sqlalchemy.orm import Session, sessionmaker

from utils.envs import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Manager:
    def __init__(self):
        self.db: Session = SessionLocal()

    def __set_name__(self, owner, name):
        self.model = owner

    def __del__(self):
        self.db.close()
        self.db = None

    def all(self):
        return self.db.query(self.model).all()

    def get(self, pk: int):
        return self.db.get(self.model, pk)

    def __save(self, instance):
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)

    def create(self, payload: dict):
        instance = self.model(**payload)
        self.__save(instance)
        return instance

    def filter(self, options: dict):
        return self.db.query(self.model).filter_by(**options).all()

    def update(self, payload: dict):
        pk = payload.pop('id', None)
        instance = self.get(pk)
        if not instance:
            raise Exception('object not found')
        for k, v in payload.items():
            if hasattr(instance, k):
                setattr(instance, k, v)
        self.__save(instance)
        return instance

    def delete(self, pk: int):
        instance = self.get(pk)
        self.db.delete(instance)
        self.db.commit()
        return
