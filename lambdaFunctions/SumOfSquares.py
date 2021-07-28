'''
Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which are even. Map function will calculate its square. 
Reduce will return addition of all that numbers. 

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
List after filter = [2, 4, 4, 2, 8, 10] 
List after map = [4, 16, 16, 4, 64, 100] 
Output of reduce = 204
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


def main():
    totalNumbers = int(input("Enter total number of elements:"))
    inputList = acceptNumbers(totalNumbers)

    if(len(inputList) == 0):
        return

    filteredList = list(filter(lambda num: (num % 2 == 0), inputList))
    print("Filtered List: ", filteredList)

    modifiedList = list(map(lambda num: num ** 2, filteredList))
    print("Modified List: ", modifiedList)

    result = reduce(lambda num1, num2: num1 + num2, modifiedList)
    print("Result is: ", result)


if(__name__ == "__main__"):
    main()
