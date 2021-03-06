import random
import time
from multiprocessing import Process
from threading import Thread

size = 10000000  # Number of random numbers to add to list
n_threads = 8  # Number of threads to create


def gen_random_num(count):
    for _ in range(count):
        random.random()


def single_thread():
    for _ in range(n_threads):
        gen_random_num(size)


def multithreaded():
    threads = [Thread(target=gen_random_num, args=(size,)) for _ in range(n_threads)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


def multiprocessed():
    processes = [Process(target=gen_random_num, args=(size,)) for _ in range(n_threads)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    tests = {
        "single thread ": single_thread,
        "multithreaded ": multithreaded,
        "multiprocessed": multiprocessed
    }

    print("# of threads:{}".format(n_threads))
    for name, test in tests.items():
        start = time.time()
        test()
        end = time.time()
        print("{} exe time:{}".format(name, end - start))

    # Run each function individually
    # multithreaded()
    # simple()
    # multiprocessed()
