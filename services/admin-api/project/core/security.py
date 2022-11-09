import secrets

from passlib.context import CryptContext

from project.core import config

context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
    argon2__rounds=config.get_settings().hash_rounds,
)


def generate_salt(salt_length: int = 16):
    return secrets.token_urlsafe(salt_length)


def hash_password(password):
    return context.hash(password)


def verify_password(hashed_password, guessed_password):
    return context.verify(guessed_password, hashed_password)
