def my_decorator(fun):
    def wrapper():
        print("before the function")
        fun()
        print("after the function")
    return wrapper
@my_decorator
def greet():
    print("hellow every one")

greet()