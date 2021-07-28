from AcceptNumbers import *


def main():
    num = int(input("Enter number of elements: "))
    if(num <= 0):
        print("Enter positive number")
        return

    numList = acceptNNumbers(num)

    checkNum = int(input("Enter number to be searched: "))

    print("Frequency of given number is:", numList.count(checkNum))


if(__name__ == "__main__"):
    main()
