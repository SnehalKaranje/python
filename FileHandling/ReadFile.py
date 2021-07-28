import os


def readFile(fileName):
    if(os.path.exists(fileName) and os.path.isfile(fileName)):
        fObj = open(fileName, "r")
        print(fObj.read())
        fObj.close()
        return

    print("File does not exists in current directory!")


def main():
    readFile(input("Enter file name: "))


if(__name__ == "__main__"):
    main()
