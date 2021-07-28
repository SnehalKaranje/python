import sys
import os
from myLogging import *

myLogging.setFileName("ChangeExtension.log")
myLogging.setBasicConfig()


def changeExtension(dirName, fileExtension1, fileExtension2):
    if(os.path.isabs(dirName) == False):
        dirName = os.path.abspath(dirName)
        logging.debug("Setting absolute directory path to " + dirName)

    if(os.path.isdir(dirName) == False):
        logging.error("Failed to find directory " + dirName)
        return

    for dir, subDirs, files in os.walk(dirName):
        for file in files:
            if(file.endswith(fileExtension1)):
                newFile = file.replace(fileExtension1, fileExtension2)
                logging.debug("Renaming file " + file + " to " + newFile)
                os.rename(os.path.join(dir, file), os.path.join(dir, newFile))


def main():
    if(len(sys.argv) < 4):
        if(len(sys.argv) == 2 and sys.argv[1].lower() == "-h"):
            print("This program changes extension of a file")
            return
        elif(len(sys.argv) == 2 and sys.argv[1].lower() == "-u"):
            print("Please enter command in following format:")
            print("python file.py directory extension1 extension2")
            print("file.py : program to be executed")
            print(
                "directory : Names of the directory in which file needs to be searched.")
            print("extension1 : extension of a file that will be searched")
            print(
                "extension2 : extension with which original file extension will be replaced")
            return
        else:
            print("Invalid number of arguments!")
            print("Use -h or -u.")
            return
    try:
        logging.info("Changing extension of files from " +
                     sys.argv[2] + " to " + sys.argv[3] + " that are present in directory " + sys.argv[1])
        changeExtension(sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as e:
        logging.error("Exception while changing extension of files" + e)


if __name__ == "__main__":
    main()
