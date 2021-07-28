def numOfDigits(num):
    count = 0
    while(int(num) != 0):
        count += 1
        num = int(num) // 10
    return count


def main():
    if(__name__ == "__main__"):
        print("Enter number:")
        num = input()
        print(numOfDigits(num))


main()
