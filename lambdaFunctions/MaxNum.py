'''
Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will 
return Maximum number from that numbers. (You can also use normal functions instead of 
lambda functions). 

Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
List after filter = [2, 11, 17, 23, 31] 
List after map = [4, 22, 34, 46, 62] 
Output of reduce = 62
'''

from functools import reduce


def acceptNumbers(totalNumbers):
    inputList = []

    if(totalNumbers <= 0):
        return inputList

    for i in range(totalNumbers):
        print("Enter num", i, end=" ")
        inputList.append(int(input()))
    return inputList


def chkPrime(num):
    if(num <= 1):
        return False
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True


def modifyNumber(num):
    return num * 2


def maxNum(num1, num2):
    if(num1 > num2):
        return num1
    return num2


def main():
    totalNumbers = int(input("Enter total number of elements:"))
    inputList = acceptNumbers(totalNumbers)

    if(len(inputList) == 0):
        return

    filteredList = list(filter(chkPrime, inputList))
    print("Filtered List: ", filteredList)

    modifiedList = list(map(modifyNumber, filteredList))
    print("Modified List: ", modifiedList)

    result = reduce(maxNum, modifiedList)
    print("Result is: ", result)


if(__name__ == "__main__"):
    main()
