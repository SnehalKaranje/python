import os


def searchFile(fileName, string):
    fObj = open(fileName, "r")
    fileContent = fObj.read()
    fObj.close()

    return fileContent.count(string)


def main():
    fileName = input("Enter file name: ")
    string = input("Enter string to be searched in file: ")

    fileExist = os.path.exists(fileName) and os.path.isfile(fileName)
    if(fileExist == False):
        print("File " + fileName + " does not exist!")
        return

    count = searchFile(fileName, string)
    print("Count : ", count)


if(__name__ == "__main__"):
    main()
