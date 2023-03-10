from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(raw_password: str):
    return pwd_context.hash(raw_password)


def check_password(raw_password: str, hashed_password: str):
    return pwd_context.verify(raw_password, hashed_password)
