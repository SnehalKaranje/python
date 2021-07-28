import os


def checkIfFileExist(fileName):
    flag = False
    if(os.path.exists(fileName)):
        if(os.path.isfile(fileName)):
            print("File exists in current directory.")
        else:
            print(fileName + " is not a file.")
    else:
        print(fileName + " does not exist in current directory")


def main():
    checkIfFileExist(input("Enter file name: "))


if(__name__ == "__main__"):
    main()
