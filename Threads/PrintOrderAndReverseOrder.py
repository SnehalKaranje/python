import threading


def printOrder(numbers, lock):
    lock.acquire()
    for i in range(1, numbers + 1):
        print(i)
    lock.release()


def printReverseOrder(numbers, lock):
    lock.acquire()
    for i in range(numbers, 0, -1):
        print(i)
    lock.release()


def main():
    lock = threading.Lock()

    thread1 = threading.Thread(target=printOrder, args=(50, lock))
    thread2 = threading.Thread(target=printReverseOrder, args=(50, lock))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if(__name__ == "__main__"):
    main()
