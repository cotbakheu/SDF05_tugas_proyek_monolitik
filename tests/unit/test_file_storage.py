import json
from pathlib import Path
from user.adapters.file_storage import load_users, save_users


def test_load_users_returns_empty_list_when_file_not_found(tmp_path: Path):
    missing_file = tmp_path / "nonexistent.json"
    result = load_users(missing_file)
    assert result == []


def test_save_and_load_users(tmp_path: Path):
    target_file = tmp_path / "users.json"
    sample_users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
    ]

    save_users(sample_users, target_file)

    assert target_file.exists()
    loaded = load_users(target_file)
    assert loaded == sample_users


def test_save_users_indentation_and_encoding(tmp_path: Path):
    target_file = tmp_path / "users.json"
    sample_users = [{"id": 1, "name": "Chloë", "email": "chloe@example.com"}]

    save_users(sample_users, target_file)

    raw_text = target_file.read_text(encoding="utf-8")
    assert "  \"name\": \"Chloë\"" in raw_text


def test_load_users_raises_json_decode_error_on_corrupt_file(tmp_path: Path):
    import pytest
    corrupt_file = tmp_path / "corrupt.json"
    corrupt_file.write_text("invalid json content", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        load_users(corrupt_file)
