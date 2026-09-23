def validate_user(name, email):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    if "@" not in email:
        raise ValueError("Invalid email")

    return {
        "name": name.strip(),
        "email": email.strip().lower(),
    }