def login(username, password):
    if len(password) < 6:
        print("Passwordtoo short")
    elif username == "admin" and password == "admin123":
        print("Login successful")
    else:
        print("Invalid credentials")
