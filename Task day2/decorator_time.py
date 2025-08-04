import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time taken: {end - start:.2f} seconds")
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function finished")

slow_function()
