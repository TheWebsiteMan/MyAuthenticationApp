updatelogin = 0
current_user = ""

def login():
    global current_user
    while True:
        user = input("Username: ")
        password = input("Password: ")
        with open("plain_text.txt", "r") as file:
            for line in file: 
                user_t, password_t = line.rstrip().split(",")
                if user == user_t and password == password_t:
                    current_user = user
                    print(f"Welcome, {user}!")
                    return 
            print("Incorrect username or password.")

def register():
    while True:
        user = input("Username: ")
        password = input("Password: ")
        with open("plain_text.txt", "r") as file:
            lines = file.readlines()
            for line in lines: 
                user_t, password_t = line.rstrip().split(",")
                if user != user_t:
                    if len(password) > 3:
                        with open("plain_text.txt", "a") as file:
                            file.write("\n")
                            file.write(f"{user},{password}")
                        print("Registered!")
                        return 
                    else:
                        print("Error: Password must be at least 4 characters")
                else:
                    print("Error: Username already taken")
                    # code doesnt work because the not user_t only checks once

def changepass():
    global current_user
    with open("plain_text.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            user_t, password_t = line.rstrip().split(",")
            if current_user == user_t:
                new_pass = input("New password: ")
                if len(new_pass) > 3:
                    with open("plain_text.txt", "a") as file:
                        file.write("\n")
                        file.write(f"{user_t},{new_pass}")
                        #remove old password
                else:
                    print("Error: Password must be at least 4 characters")
        


def menu_logic():
    global updatelogin
    if updatelogin == 0:
        print("1. Login")
        print("2. Register")
        print("3. Quit")
        l1 = input(": ")
        match l1:
            case "1":
                login()
                updatelogin = 1
                return
            case "2":
                register()
                return
            case "3":
                print("Goodbye!")
                return 7
            case _:
                return
    else:
        print("1: Change password")
        print("2: Logout")
        l2 = input(": ")
        match l2:
            case "1":
                changepass()
                return
            case "2":
                print("Goodbye!")
                return 7
            case _:
                return

def menu():
    while True:
        if menu_logic() == 7:
            break


def main():
    menu()

main()