from AcceptNumbers import *


def main():
    num = int(input("Enter number of elements: "))
    if(num <= 0):
        print("Enter positive number")
        return

    numList = acceptNNumbers(num)
    print("Maximum of given numbers is:", max(numList))


if(__name__ == "__main__"):
    main()
