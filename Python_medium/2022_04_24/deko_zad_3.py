from datetime import datetime


def time_before_and_after(func):
    def wrapper():
        print(datetime.now().strftime("%H:%M:%S"))
        func()
        print(datetime.now().time())
    return wrapper


@time_before_and_after
def hello_world():
    print("Hello world")


hello_world()