import sys
import os
from myLogging import *

myLogging.setFileName("SearchFiles.log")
myLogging.setBasicConfig()


def findFiles(directory, fileExtension):
    if(os.path.isabs(directory) == False):
        directory = os.path.abspath(directory)
        logging.debug("Setting absolute path of directory to : " + directory)

    if(os.path.isdir(directory) == False):
        logging.error("Directory " + directory + " not found")
        return

    for dir, subDirs, files in os.walk(directory):
        for fileName in files:
            if(fileName.endswith(fileExtension)):
                logging.info("Found file : " + fileName)


def main():
    if(len(sys.argv) < 3):
        if(len(sys.argv) == 2 and sys.argv[1].lower() == "-h"):
            print(
                "This program returns list of files with given extension in the directory")
            return
        elif(len(sys.argv) == 2 and sys.argv[1].lower() == "-u"):
            print("Please enter command in following format:")
            print("python file.py directory fileExtension")
            print("file.py : program to be executed")
            print(
                "directory : Names of the directory in which file needs to be searched.")
            print("fileExtension : extension of a file")
            return
        else:
            print("Invalid number of arguments!")
            print("Use -h or -u.")
            return

    try:
        logging.info("Finding files with extension " +
                     sys.argv[2] + " in directory " + sys.argv[1])
        findFiles(sys.argv[1], sys.argv[2])
    except Exception as e:
        logging.error("Exception while finding files " + e)


if __name__ == "__main__":
    main()
