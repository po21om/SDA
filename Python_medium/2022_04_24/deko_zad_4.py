
def retry(how_many=3):
    def retry_inside(func):
        def wrapper(*args, **kwargs):
            for _ in range(how_many):
                try:
                    func(*args, **kwargs)
                except Exception:
                    pass
        return wrapper
    return retry_inside

@retry(24)
def hello_world(what_to_print):
    print(what_to_print)


hello_world("GOGOGO")