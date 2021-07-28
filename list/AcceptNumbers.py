def acceptNNumbers(totalNumbers):
    numList = []
    for i in range(totalNumbers):
        print("Enter num", i, end=' ')
        num = int(input())
        numList.append(num)
    return numList
