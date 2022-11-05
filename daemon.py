# daemon thread - a thread that run in the background, not important for program to run. Program will not wait for
# daemon threads to complete before exiting non-daemon threads cannot normally be killed, stay alive until task is
# complete. For example: background tasks, garbage collection, waiting for input, long-running processes

import time
import threading


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for:", count, "s")


x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you want to exit?")
