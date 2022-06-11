
def cache(func):
    def wrapper(*args, **kwargs):
        with open("cache.txt","a") as f:
            f.write(f'{func(*args, **kwargs)}\n')
        print(func(*args, **kwargs))
    return wrapper


@cache
def hello_world(what_to_print):
    return what_to_print


hello_world("GoGoGo")
hello_world("JOhnny")


@cache
def divider(a,b):
    return a/b


divider(10, 5)
