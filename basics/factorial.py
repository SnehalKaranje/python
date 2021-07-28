def factorial(num):
    fact = 1
    for i in range(1, int(num) + 1):
        fact *= i
    return fact


def main():
    if(__name__ == "__main__"):
        print("Enter number:")
        num = input()
        print(factorial(num))


main()
