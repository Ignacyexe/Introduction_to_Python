# multiprocessing running tasks in parallel in different cpu cores, bypasses all GIL used for threading.
# it is preferred cpu bound tasks which require big cpu usage in opposite multithreading are better for waiting tasks

from multiprocessing import Process, cpu_count
import time

start = time.perf_counter()


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print(cpu_count())

    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()   # process synchronization by join function
    b.join()
    c.join()
    d.join()

    print("Finished in:", time.perf_counter() - start, "s")


if __name__ == "__main__":   # when we create child process it will copy it, not execute it
    main()
