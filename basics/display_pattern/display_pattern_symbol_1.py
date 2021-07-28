def displayPattern(num):
    for i in range(int(num)):
        for j in range(int(num)):
            print("*", end=' ')
        print("\r")


def main():
    if(__name__ == "__main__"):
        print("Enter number:")
        num = input()
        displayPattern(num)


main()
