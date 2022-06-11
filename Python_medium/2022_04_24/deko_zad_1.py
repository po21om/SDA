from datetime import datetime

def only_while_day(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper


@only_while_day
def hello_world():
    print("Hello world")

hello_world()