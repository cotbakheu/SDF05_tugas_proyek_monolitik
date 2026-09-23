from typing import Callable, Optional
from user.adapters.file_storage import load_users as default_load_users
from user.adapters.file_storage import save_users as default_save_users

try:
    from user.domain.rules import validate_user as default_validate_user
except ImportError:
    default_validate_user = None


def create_user(
    name: str,
    email: str,
    loader: Callable = default_load_users,
    saver: Callable = default_save_users,
    validator: Optional[Callable] = None,
) -> dict:
    validate_func = validator or default_validate_user
    if validate_func is None:
        raise RuntimeError("No validator provided and domain rules not found")

    users = loader()
    user = validate_func(name, email)

    if any(existing.get("email") == user["email"] for existing in users):
        raise ValueError("Email already exists")

    next_id = max((existing.get("id", 0) for existing in users), default=0) + 1
    user["id"] = next_id
    users.append(user)
    saver(users)

    return user


def list_users(loader: Callable = default_load_users) -> list[dict]:
    return loader()
