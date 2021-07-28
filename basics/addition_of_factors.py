def additionOfFactors(num):
    sum = 0
    for i in range(1, int(num) + 1):
        if(int(num) % i == 0):
            sum += i
    return sum


def main():
    if(__name__ == "__main__"):
        print("Enter number:")
        num = input()
        print(additionOfFactors(num))


main()
