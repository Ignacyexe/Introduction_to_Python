# thread - a flow of execution. Like a separate order of instructions. However, each thread takes a turn running to
# achieve concurrency GIL (global interpreter lock), allows only one thread to hold the control of the python
# interpreter at any one time

# cpu bound - program/task spends most of it's time waiting for internal events (CPU intensive) use multiprocessing

# io bound - program/task spends most of it's time waiting for external events (user input) use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast!")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee!")


def study():
    time.sleep(5)
    print("You have studied!")


# without threading these three functions will execute sequentially, one by another.
# with this piece of code we can run program concurrently instead sequentially

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# x.join()   # with that function main thread must wait until these threads will synchronise and join.
# y.join()
# z.join()

# eat_breakfast()
# drink_coffee()
# study()

print()
print(threading.active_count())   # these two functions were called before that three functions, because they are
print(threading.enumerate())      # executed by main thread, and it's not going to wait for others to complete
print(time.perf_counter())
