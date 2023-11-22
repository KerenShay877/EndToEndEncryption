users = {}

def register(username, password):
    if username not in users:
        users[username] = password
        print(f"User {username} registered successfully.")
    else:
        print(f"User {username} already exists.")

def login(username, password):
    if username in users and users[username] == password:
        print(f"User {username} logged in successfully.")
    else:
        print("Invalid username or password.")