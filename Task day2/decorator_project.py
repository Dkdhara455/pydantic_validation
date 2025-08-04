import time
from functools import wraps

LOG_FILE = "Task day2\ log.txt"

# ✅ Decorator definition
def log_and_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        log_entry = (
            f"Function: {func.__name__}\n"
            f"Arguments: {args} {kwargs}\n"
            f"Returned: {result}\n"
            f"Execution time: {end - start:.4f} seconds\n"
            f"{'-'*40}\n"
        )

        print(log_entry)  # Optional: comment out if you only want file logging

        # ✅ Write log to file
        with open(LOG_FILE, "a") as file:
            file.write(log_entry)

        return result
    return wrapper

# ✅ Test functions using the decorator
@log_and_time
def add(a, b):
    time.sleep(1)
    return a + b

@log_and_time
def greet(name):
    time.sleep(0.5)
    return f"Hello, {name}!"

@log_and_time
def multiply(a, b=1):
    return a * b

# ✅ Calling the functions
add(5, 7)
greet("Deepak")
multiply(3, b=4)
