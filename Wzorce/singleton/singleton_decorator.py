def singleton(class_):
    __instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]
    return get_instance


@singleton
class FirstClass:
    def __init__(self):
        self.val: int = 0

@singleton
class SecondClass:
    def __init__(self):
        self.val: int = 0



if __name__ == '__main__':
    e = FirstClass()
    print(e.val)
    e.val = 10
    print(e.val)
    f = FirstClass()
    print(f.val)
    f.val = 15
    print(e.val)
    print(f.val)

    g = SecondClass()
    print(g.val)
    