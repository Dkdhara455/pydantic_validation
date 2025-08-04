import time

# ✅ Decorator to log function calls
def log_action(func):
    def wrapper(user):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S")
        result = func(user)
        log = f"[{time_now}] {user} called {func.__name__} → {result}\n"
        
        # Save to file
        with open("Task day2\ log1.txt", "a",encoding="utf-8") as file:
            file.write(log)

        print(log.strip())  # Optional: also show on screen
        return result
    return wrapper

# ✅ Example functions (user actions)
@log_action
def login(user):
    return "logged in"

@log_action
def logout(user):
    return "logged out"

@log_action
def delete_account(user):
    return "account deleted"

# ✅ Simulate actions
login("alice")
logout("alice")
delete_account("bob")
