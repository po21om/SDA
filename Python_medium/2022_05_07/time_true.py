import time

while True:
    localtime = time.localtime()
    print(time.strftime('%T:%M:%S', localtime))

    time.sleep(1)