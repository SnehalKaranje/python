def chkPrimeNumber(num):
    if(int(num) <= 1):
        print("Not a prime number")
        return

    for i in range(2, int(num)):
        if(int(num) % i == 0):
            print("It is not a prime number")
            return

    print("It is a prime number")


def main():
    if(__name__ == "__main__"):
        print("Enter number:")
        num = input()
        chkPrimeNumber(num)


main()
