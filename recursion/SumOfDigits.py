def sumOfDigits(num):
    if(num == 0):
        return num
    return num % 10 + sumOfDigits(num//10)


def main():
    num = int(input("Enter number: "))
    print("Sum of digits: ", sumOfDigits(num))


if (__name__ == "__main__"):
    main()
