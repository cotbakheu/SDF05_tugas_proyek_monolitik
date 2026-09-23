import json
from pathlib import Path
from typing import Union

DEFAULT_FILE = Path("users.json")


def load_users(file_path: Union[Path, str] = DEFAULT_FILE) -> list[dict]:
    path = Path(file_path)
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users: list[dict], file_path: Union[Path, str] = DEFAULT_FILE) -> None:
    path = Path(file_path)
    with path.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=2, ensure_ascii=False)
