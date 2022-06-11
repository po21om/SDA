import os

def istnieje():
    if os.path.exists("c:\\Users\\barba\\PycharmProjects"):
        return 50
    else:
        return 200

if __name__ == '__main__':
    a = istnieje()
    print(a)
    print(type(a))