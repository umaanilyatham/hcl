'''import threading

import time


def check_log():

    for i in range(3):

        print("Checking log...")

        time.sleep(1)

def check_cpu():
    for i in range(3):
        print("Checking CPU...")

        time.sleep(1)

thread1 = threading.Thread(target=check_log)
thread2 = threading.Thread(target=check_cpu)

thread1.start()
thread2.start()

# Joining threads to the main thread
thread1.join()
thread2.join()'''


def add(*args):
    total = 0
    for num in args:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
result = add(*numbers)  
print(result)  # Output: 15