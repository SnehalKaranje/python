import sys
import os


def compareFile(file1, file2):
    file1Exist = os.path.exists(file1) and os.path.isfile(file1)
    if(file1Exist == False):
        print("File " + file1 + " does not exist!")
        return

    file2Exist = os.path.exists(file2) and os.path.isfile(file2)
    if(file2Exist == False):
        print("File " + file2 + " does not exist!")
        return

    flag = True

    fObj1 = open(file1, "r")
    fObj2 = open(file2, "r")

    f1Line = fObj1.readline()
    f2Line = fObj2.readline()

    while f1Line != '' or f2Line != '':
        f1Line = f1Line.rstrip()
        f2Line = f2Line.rstrip()

        if(f1Line != f2Line):
            flag = False

        f1Line = fObj1.readline()
        f2Line = fObj2.readline()

    fObj1.close()
    fObj2.close()

    if(flag):
        print("Success!")
    else:
        print("Failure!")


def main():
    if(len(sys.argv) < 3):
        if(len(sys.argv) == 2 and sys.argv[1].lower() == "-h"):
            print("This program compares contents of files")
            return
        elif(len(sys.argv) == 2 and sys.argv[1].lower() == "-u"):
            print("Please enter command in following format:")
            print("python file.py fileName1 fileName2")
            print("file.py : program to be executed")
            print("fileName1 and fileName2 : Names of the file to be compared")
            return
        else:
            print("Invalid number of arguments!")
            print("Use -h or -u.")
            return

    compareFile(sys.argv[1], sys.argv[2])


if(__name__ == "__main__"):
    main()
