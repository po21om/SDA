# odliczanie
import timeit

def counting(_from, _to):
    while _from >= _to:
        _from -= 1


def wo_threading(_from, _to):
    while _from >= _to:
        _from -= 1


def with_threading(_from, _to):
    import threading

    thread_1 = threading.Thread(target=counting, args=(_from, _from / 2))
    thread_2 = threading.Thread(target=counting, args=(_from / 2, _to))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

def with_multiproc(_from, _to):
    import multiprocessing

    mproc_1 = multiprocessing.Process(target=counting, args=(_from, _from / 2))
    mproc_2 = multiprocessing.Process(target=counting, args=(_from / 2, _to))

    # mproc_1.start()
    # mproc_2.start()
    #
    # mproc_1.join()
    # mproc_2.join()

if __name__ == "__main__":
    wo_threading_1 = "wo_threading(400000, 0)"
    with_threading_1 = "with_threading(400000, 0)"
    with_multiproc_1 = "with_multiproc(400000, 0)"

    setup = 'from __main__ import wo_threading, with_threading, with_multiproc'

    print("Bez watkow:", timeit.timeit(stmt=wo_threading_1,
                                           setup=setup,
                                           number=1))
    print("Z watkami", timeit.timeit(stmt=with_threading_1,
                                         setup=setup,
                                         number=1))
    print("Z podproc", timeit.timeit(stmt=with_multiproc_1,
                                     setup=setup,
                                     number=1))