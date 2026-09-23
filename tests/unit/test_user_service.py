import pytest
from user.services.user_service import create_user, list_users


def test_list_users():
    mock_users = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]
    result = list_users(loader=lambda: mock_users)
    assert result == mock_users


def test_create_user_success():
    saved_state = []

    def mock_loader():
        return list(saved_state)

    def mock_saver(users):
        saved_state.clear()
        saved_state.extend(users)

    user = create_user(
        name=" Alice ",
        email="Alice@Example.com",
        loader=mock_loader,
        saver=mock_saver,
    )

    assert user == {"id": 1, "name": "Alice", "email": "alice@example.com"}
    assert len(saved_state) == 1
    assert saved_state[0] == user


def test_create_user_sequential_id():
    saved_state = [{"id": 5, "name": "Existing", "email": "existing@example.com"}]

    def mock_loader():
        return list(saved_state)

    def mock_saver(users):
        saved_state.clear()
        saved_state.extend(users)

    user = create_user(
        name="Bob",
        email="bob@example.com",
        loader=mock_loader,
        saver=mock_saver,
    )

    assert user["id"] == 6


def test_create_user_duplicate_email_raises_error():
    existing = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]
    with pytest.raises(ValueError, match="Email already exists"):
        create_user(
            name="Alice Duplicate",
            email="alice@example.com",
            loader=lambda: existing,
            saver=lambda u: None,
        )


def test_create_user_validation_error_propagates():
    with pytest.raises(ValueError, match="Invalid email"):
        create_user(
            name="Alice",
            email="notanemail",
            loader=lambda: [],
            saver=lambda u: None,
        )
