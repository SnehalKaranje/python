def sumOfDigits(num):
    sum = 0
    while(int(num) != 0):
        digit = int(num) % 10
        sum += digit
        num = int(num) // 10
    return sum


def main():
    if(__name__ == "__main__"):
        print("Enter number:")
        num = input()
        print(sumOfDigits(num))


main()
