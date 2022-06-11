import timeit


# odliczanie
def odliczanka(_od, _do):
    while _od >= _do:
        _od -= 1


def bez_watkow(_od, _do):
    while _od >= _do:
        _od -= 1


def z_watkami(_od, _do):
    import threading

    watek_1 = threading.Thread(target=odliczanka, args=(_od, _od/2))
    watek_2 = threading.Thread(target=odliczanka, args=(_od/2, _do))

    # tutaj startujemy watki
    watek_1.start()
    watek_2.start()

    # tutaj czekamy z egzekucja na zakonczenie watkow
    watek_1.join()
    watek_2.join()


def z_podprocesami(_od, _do):
    import multiprocessing

    podproces_1 = multiprocessing.Process(target=odliczanka, args=(_od, _od/2))
    podproces_2 = multiprocessing.Process(target=odliczanka, args=(_od/2, _do))

    podproces_1.start()
    podproces_2.start()

    podproces_1.join()
    podproces_2.join()

# bez_watkow(400000, 0)
# z_watkami(400000, 0)

if __name__ == "__main__":
    wo_threading = "bez_watkow(1000000000, 0)"
    with_threading = "z_watkami(1000000000, 0)"
    with_multiprocessing = "z_podprocesami(1000000000, 0)"
    setup = "from __main__ import bez_watkow, z_watkami, z_podprocesami"

    print("Bez watkow:", timeit.timeit(stmt=wo_threading,
                                       setup=setup,
                                       number=1))
    print("Z watkami:", timeit.timeit(stmt=with_threading,
                                      setup=setup,
                                      number=1))
    print("Z podprocesami:", timeit.timeit(stmt=with_multiprocessing,
                                           setup=setup,
                                           number=1))