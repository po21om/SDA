from datetime import datetime


def only_when_you_want_it(a=0, b=24):
    def inside(func):
        def wrapper():
            if a <= datetime.now().hour < b:
                func()
        return wrapper
    return inside


@only_when_you_want_it(7,12)
def hello_world():
    print("Hello world")


hello_world()