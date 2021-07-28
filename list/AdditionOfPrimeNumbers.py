import Prime


def additionOfPrimeNum(numList):
    sum = 0
    for num in numList:
        if(Prime.ChkPrime(num)):
            sum += num
    return sum


def ListPrime(totalNumbers):
    numList = []
    for i in range(totalNumbers):
        print("Enter num", i, end=' ')
        num = int(input())
        numList.append(num)
    return numList


def main():
    num = int(input("Enter number of elements: "))
    if(num <= 0):
        print("Enter positive number")
        return

    numList = ListPrime(num)

    print("Addition of prime numbers is: ", additionOfPrimeNum(numList))


if(__name__ == "__main__"):
    main()
