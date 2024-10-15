import getpass

def signup():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    with open("user-enc.txt", "w") as f:
        f.write(f"{username}:{password}")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    with open("user-enc.txt", "r") as f:
        stored_credentials = f.read().strip()
        if stored_credentials == f"{username}:{password}":
            print("Login successful.")
        else:
            print("Wrong username or password.")

while True:
    print("1. Sign up\n2. Login\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        signup()
    elif choice == '2':
        login()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")
