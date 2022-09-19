from config import Config
import hashlib


def get_password_hash(password: str) -> str:
    return hashlib.sha512(str(password + Config.salt).encode("utf-8")).hexdigest()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return get_password_hash(plain_password) == hashed_password
