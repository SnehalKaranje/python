from AcceptNumbers import *


def addition(numList):
    sum = 0
    for num in numList:
        sum += num
    return sum


def main():
    num = int(input("Enter number of elements: "))
    if(num <= 0):
        print("Enter positive number")
        return

    numList = acceptNNumbers(num)
    print("Addition of given numbers is:", addition(numList))


if(__name__ == "__main__"):
    main()
