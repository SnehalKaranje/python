import threading


def displayEvenNumbers(totalNumbers):
    for num in range(1, totalNumbers * 2 + 1):
        if(num % 2 == 0):
            print(num)


def displayOddNumbers(totalNumbers):
    for num in range(1, totalNumbers * 2 + 1):
        if(num % 2 != 0):
            print(num)


def main():
    thread1 = threading.Thread(target=displayEvenNumbers, args=(10,))
    thread2 = threading.Thread(target=displayOddNumbers, args=(10,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if(__name__ == "__main__"):
    main()
