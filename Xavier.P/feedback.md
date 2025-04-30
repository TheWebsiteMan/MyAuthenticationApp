# Feedback

### **Strengths**
1. **Basic Functionality**:
   - The code implements login, registration, and password change features.
   - It uses a menu system to guide the user through different options.

2. **File-Based User Storage**:
   - Usernames and passwords are stored in a file (`plain_text.txt`), allowing data persistence.

3. **Separation of Concerns**:
   - Functions like `login`, `register`, and `changepass` handle specific tasks, improving readability.

---

### **Issues and Suggestions for Improvement**

#### 1. **Plain Text Password Storage**
   - Storing passwords in plain text (`plain_text.txt`) is a major security flaw.

   **Fix**: Use password hashing (e.g., `bcrypt`) to securely store passwords.

   Example:
   ```python
   import bcrypt

   salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

   # Hashing a password
   hashed_password = bcrypt.hashpw(password.encode(), salt=salt)

   # Verifying a password
   if bcrypt.checkpw(input_password.encode(), hashed_password):
       print("Login successful!")
   ```

---

#### 2. **Inefficient User Lookup**
   - The code reads the entire file line by line for every login, registration, and password change operation, which is inefficient.

   **Fix**: Load the file into memory once and use a dictionary for faster lookups.

   Example:
   ```python
   def load_users():
       users = {}
       with open("plain_text.txt", "r") as file:
           for line in file:
               user, password = line.strip().split(",")
               users[user] = password
       return users
   ```

---

#### 3. **Registration Logic Issues**
   - The `register` function has a bug where it only checks the first username in the file for duplicates.
   - It also appends a newline (`\n`) before writing the new user, which could lead to formatting issues.

   **Fix**: Check all usernames for duplicates and ensure proper file formatting.

   Example:
   ```python
   def register(users):
       user = input("Username: ").strip()
       if user in users:
           print("Error: Username already taken")
           return
       password = input("Password: ").strip()
       if len(password) < 4:
           print("Error: Password must be at least 4 characters")
           return
       users[user] = hash_password(password)
       with open("plain_text.txt", "a") as file:
           file.write(f"{user},{users[user]}\n")
       print("Registered!")
   ```

---

#### 4. **Password Change Logic Issues**
   - The `changepass` function appends the new password to the file instead of replacing the old one.
   - This results in multiple entries for the same user.

   **Fix**: Rewrite the file with the updated password.

   Example:
   ```python
   def changepass(users):
       global current_user
       if current_user not in users:
           print("Error: User not logged in")
           return
       new_pass = input("New password: ").strip()
       if len(new_pass) < 4:
           print("Error: Password must be at least 4 characters")
           return
       users[current_user] = hash_password(new_pass)
       with open("plain_text.txt", "w") as file:
           for user, password in users.items():
               file.write(f"{user},{password}\n")
       print("Password updated!")
   ```

---

#### 5. **Global Variables**
   - The use of global variables (`updatelogin` and `current_user`) makes the code harder to debug and maintain.

   **Fix**: Pass these variables as arguments to functions or encapsulate them in a class.

---

#### 6. **No Input Validation**
   - The code does not validate user input, which could lead to unexpected behavior or errors.

   **Fix**: Add input validation to ensure usernames and passwords meet certain criteria (e.g., no special characters, minimum length).

---

#### 7. **No Error Handling**
   - The code does not handle errors, such as file not found or invalid file format.

   **Fix**: Add error handling using `try` and `except` blocks.

   Example:
   ```python
   try:
       with open("plain_text.txt", "r") as file:
           # File operations
   except FileNotFoundError:
       print("Error: User file not found.")
   ```

---

#### 8. **No Logout State**
   - After logging out, the `current_user` variable is not reset, which could lead to unintended behavior.

   **Fix**: Reset `current_user` to an empty string on logout.

---

#### 9. **No Exit Condition for Menu**
   - The `menu_logic` function does not properly handle the "Quit" option, as it relies on returning `7` to exit.

   **Fix**: Use a more intuitive approach, such as a `while` loop with a `break` condition.