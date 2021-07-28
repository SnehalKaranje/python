def printPattern(num):
    for i in range(int(num)):
        for j in range(1, int(num)+1):
            print(j, end=' ')
        print("\r")


def main():
    if(__name__ == "__main__"):
        print("Enter number:")
        num = input()
        printPattern(num)


main()
