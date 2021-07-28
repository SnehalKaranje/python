import threading


def small(inputString):
    print("Thread: " + threading.current_thread().name +
          " Id: " + str(threading.current_thread().ident))
    sum = 0
    for i in inputString:
        if(i.islower()):
            sum += 1
    print("number of small case characters: ", sum)


def capital(inputString):
    print("Thread: " + threading.current_thread().name +
          " Id: " + str(threading.current_thread().ident))
    sum = 0
    for i in inputString:
        if(i.isupper()):
            sum += 1
    print("number of upper case characters: ", sum)


def digit(inputString):
    print("Thread: " + threading.current_thread().name +
          " Id: " + str(threading.current_thread().ident))
    sum = 0
    for i in inputString:
        if(i.isdigit()):
            sum += 1
    print("number of digits: ", sum)


def main():
    inputString = input("Enter string: ")

    thread1 = threading.Thread(target=small, args=(inputString,))
    thread2 = threading.Thread(target=capital, args=(inputString,))
    thread3 = threading.Thread(target=digit, args=(inputString,))

    thread1.setName('small')
    thread2.setName('capital')
    thread3.setName('digit')

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


if(__name__ == "__main__"):
    main()
