def my_print(prefix, *args, **kwargs):
    print(prefix)
    if kwargs.get('ile_razy'):
        for _ in range(kwargs.get('ile_razy')):
            print(*args)
    else:
        print(*args)



if __name__ == '__main__':
    my_print("Starting", "a", "b", "c", ile_razy=6)
