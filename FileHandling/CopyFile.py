import sys
import os


def copyFile(file1):
    file1Exist = os.path.exists(file1) and os.path.isfile(file1)
    if(file1Exist == False):
        print("File " + file1 + " does not exist!")
        return

    fObj1 = open(file1, "r")
    fObj2 = open("Demo.txt", "w")

    fObj2.write(fObj1.read())
    print("Contents copied!")

    fObj1.close()
    fObj2.close()


def main():
    if(len(sys.argv) < 2):
        print("Invalid number of arguments!")
        print("Use -h or -u.")
        return

    elif(len(sys.argv) == 2 and sys.argv[1].lower() == "-h"):
        print("This program copies contents of file in Demo.txt")
        return

    elif(len(sys.argv) == 2 and sys.argv[1].lower() == "-u"):
        print("Please enter command in following format:")
        print("python file.py fileName1")
        print("file.py : program to be executed")
        print("fileName1 : Names of the file to be copied in Demo.txt")
        return

    copyFile(sys.argv[1])


if(__name__ == "__main__"):
    main()
