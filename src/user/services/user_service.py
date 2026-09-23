from user.domain.ports import Loader, Saver
from user.domain.rules import validate_user


def create_user(
    name: str,
    email: str,
    loader: Loader,
    saver: Saver,
) -> dict:

    users = loader()
    user = validate_user(name, email)

    if any(existing.get("email") == user["email"] for existing in users):
        raise ValueError("Email already exists")

    next_id = max((existing.get("id", 0) for existing in users), default=0) + 1
    user["id"] = next_id
    users.append(user)
    saver(users)

    return user



def list_users(loader: Loader) -> list[dict]:
    return loader()
