# Napisz dekorator delay który sprawi że funkcja wykona się z 5 sekundowym opóźnieniem
from time import sleep


def delay(func):
    def wrapper(*args, **kwargs):
        sleep(5)
        return func(*args, **kwargs)
    return wrapper


@delay
def hello():
    print("Hello World!")


@delay
def div(a, b):
    return a / b


print(div(10, 5))

#dekorator z parametrem - fabryka dekoratorów - zwraca dekorator dostosowany do warotości
def delay_time(t=0):
    def delay_inside(func):
        def wrapper(*args, **kwargs):
            sleep(t)
            return func(*args, **kwargs)
        return wrapper
    return delay_inside


@delay_time(10)
def hello():
    print("Hello World!")


@delay_time(1)
def div(a, b):
    return a / b


print(div(99, 11))
