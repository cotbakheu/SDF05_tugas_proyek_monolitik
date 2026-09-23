from user.adapters.file_storage import load_users, save_users
from user.services.user_service import create_user, list_users

def create_user_interface():
    loader = lambda: load_users("users.json")
    saver = lambda users: save_users(users, "users.json")

    name = input("Name: ")
    email = input("Email: ")

    try:
        user = create_user(name, email, loader, saver)
        print(f"User created: {user}")
    except ValueError as error:
        print(f"Error: {error}")

def list_users_interface():
    loader = lambda: load_users("users.json")
    users = list_users(loader)

    if not users:
        print("No users found.")
        return

    print("List of Users:")
    for user in users:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")

def main():

    print("User Management CLI")
    print("-" * 25)
    print()
    print("1. Create User")
    print("2. List Users")
    print("3. Exit")
    print()

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        create_user_interface()
    elif choice == "2":
        list_users_interface()
    elif choice == "3":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()