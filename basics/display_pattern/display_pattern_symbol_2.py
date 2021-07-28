def printPattern(num):
    for i in range(int(num), 0, -1):
        for j in range(i, 0, -1):
            print("*", end=' ')
        print("\r")


def main():
    if(__name__ == "__main__"):
        print("Enter number:")
        num = input()
        printPattern(num)


main()
