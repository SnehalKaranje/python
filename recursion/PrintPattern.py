def printPatternSymbol(num):
    if(num == 0):
        return
    print("*", end=" ")
    printPatternSymbol(num - 1)


def printPatternNum(num):
    if(num == 0):
        return
    printPatternNum(num - 1)
    print(num, end=" ")


def main():
    num = int(input("Enter number: "))
    printPatternSymbol(num)
    printPatternNum(num)


if (__name__ == "__main__"):
    main()
