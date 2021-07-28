def factorial(num):
    if (num == 1):
        return num
    return num * factorial(num - 1)


def main():
    num = int(input("Enter number: "))
    print("Factorial of a number: ", factorial(num))


if(__name__ == "__main__"):
    main()
