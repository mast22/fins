from argon2 import PasswordHasher


def hash_pass(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)


def verify_pass(password: str, hash: str) -> bool:
    ph = PasswordHasher()
    return ph.verify(hash, password)
