import bcrypt

# Initialise global vars
salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"
current_user = ""

def load_users():
    users = {}
    with open("plain_text.txt", "r") as file:
        for line in file:
            user, password = line.strip().split(",")
            users[user] = password
    return users

def login():
    global current_user
    while True:
        user = input("Username: ")
        password = input("Password: ")
        byte_string = load_users()[user]
        byte_string = byte_string.encode('utf-8')
        if bcrypt.checkpw(password.encode(), byte_string):
            print("Login successful!")
            current_user = user
            print(f"Welcome, {user}!")
            return
        else:
            print("Incorrect username or password")

def register(users):
    user = input("Username: ").strip()
    if user in users:
        print("Error: Username already taken")
        return
    password = input("Password: ").strip()
    if len(password) < 4:
        print("Error: Password must be at least 4 characters")
        return
    users[user] = bcrypt.hashpw(password.encode(), salt=salt)
    with open("plain_text.txt", "a") as file:
        file.write(f"{user},{users[user]}\n")
    print("Registered!")

def changepass(users):
    global current_user
    if current_user not in users:
        print("Error: User not logged in")
        return
    new_pass = input("New password: ").strip()
    if len(new_pass) < 4:
        print("Error: Password must be at least 4 characters")
        return
    users[current_user] = bcrypt.hashpw(new_pass, salt=salt)
    with open("plain_text.txt", "w") as file:
        for user, password in users.items():
            file.write(f"{user},{password}\n")
    print("Password updated!")

def main():
    global current_user
    while True:
        if current_user == "":
            print("1. Login")
            print("2. Register")
            print("3. Quit")
            l1 = input(": ")
            match l1:
                case "1":
                    login()
                case "2":
                    register(load_users())
                case "3":
                    print("Goodbye!")
                    break
                case _:
                    print()
        else:
            print("1: Change password")
            print("2: Logout")
            l2 = input(": ")
            match l2:
                case "1":
                    changepass(load_users())
                case "2":
                    print("Goodbye!")
                    current_user = ""
                case _:
                    print()

main()