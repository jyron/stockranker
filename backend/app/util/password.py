"""
Password utility functions
"""

import bcrypt

from app.config import CONFIG


def hash_password(password: str) -> str:
    """Returns a salted password hash"""
    return bcrypt.hashpw(password.encode(), CONFIG.salt).decode()
