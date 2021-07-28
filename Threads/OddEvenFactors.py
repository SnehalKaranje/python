import threading
import time


def addEvenFactors(num):
    time.sleep(10)
    sum = 0
    for i in range(1, num + 1):
        if((num % i == 0) and (i % 2 == 0)):
            sum += i
    print("Addition of even factors: ", sum)


def addOddFactors(num):
    sum = 0
    for i in range(1, num + 1):
        if((num % i == 0) and (i % 2 != 0)):
            sum += i
    print("Addition of odd factors: ", sum)


def main():
    num = int(input("Enter number: "))

    thread1 = threading.Thread(target=addEvenFactors, args=(num,))
    thread2 = threading.Thread(target=addOddFactors, args=(num,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main")


if(__name__ == "__main__"):
    main()
