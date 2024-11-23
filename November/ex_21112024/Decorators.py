def decorator_1(func):
    def wrapper():
        print("Hello,")
        func()
    return wrapper()

def decorator_2(func):
    def wrapper():
        func()
        print("Good Morning")
        print("Have a Good Day")
    return wrapper()

@decorator_2
@decorator_1
def user_name():
    print("Prathyusha")
user_name()

# username = input("Enter your name:")


