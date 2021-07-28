'''
Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which greater than or equal to 70 and less than or equal to 
90. Map function will increase each number by 10. Reduce will return product of all that 
numbers. 

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 
List after filter = [76, 89, 86, 90, 70] 
List after map = [86, 99, 96, 100, 80] 
Output of reduce = 6538752000 
'''

from functools import reduce


def filterNumber(num):
    if(num >= 70 and num <= 90):
        return num


def modifyNumber(num):
    return num + 10


def multiplyNumbers(num1, num2):
    return num1 * num2


def acceptNumbers(totalNumbers):
    inputList = []

    if(totalNumbers <= 0):
        return inputList

    for i in range(totalNumbers):
        print("Enter num", i, end=" ")
        inputList.append(int(input()))
    return inputList


def main():
    totalNumbers = int(input("Enter total number of elements:"))
    inputList = acceptNumbers(totalNumbers)

    if(len(inputList) == 0):
        return

    filteredList = list(filter(filterNumber, inputList))
    print("Filtered List: ", filteredList)

    modifiedList = list(map(modifyNumber, filteredList))
    print("Modified List: ", modifiedList)

    result = reduce(multiplyNumbers, modifiedList)
    print("Result is: ", result)


if(__name__ == "__main__"):
    main()
