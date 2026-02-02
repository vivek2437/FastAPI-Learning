from passlib.context import CryptoContext

pwd_context =CryptoContext(schemas= ["argon2"] , depercated = "auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str , hashed_password: str) -> bool:
    return pwd_context.verify(plain_password , hashed_password)
