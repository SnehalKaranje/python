import sys
import os
import checksum
from myLogging import *
import time

myLogging.setFileName("Log.txt")
myLogging.setBasicConfig()


def removeDuplicates(duplicates):
    for fileList in duplicates:
        counter = 1
        for file in fileList:
            if(counter > 1):
                logging.info("Removing file %s", file)
                os.remove(file)
            counter += 1


def printDuplicates(duplicates):
    for fileList in duplicates:
        logging.info("Duplicate files : %s", fileList)


def getFileHash(path):
    fileHashMap = {}
    for dirName, subDirs, files in os.walk(path):
        logging.debug("Current directory is : %s", dirName)
        for file in files:
            filePath = os.path.join(dirName, file)
            fileHash = checksum.hashfile(filePath)
            if(fileHash in fileHashMap):
                fileHashMap[fileHash].append(filePath)
            else:
                fileHashMap[fileHash] = [filePath]

    logging.debug("Returning : %s", fileHashMap)
    return fileHashMap


def findDuplicates(path):
    fileHashMap = getFileHash(path)
    duplicates = list(filter(lambda files: len(files)
                      > 1, fileHashMap.values()))
    return duplicates


def getValidPath(path):
    if(os.path.isabs(path) == False):
        path = os.path.abspath(path)

    if(os.path.isdir(path) == False):
        logging.error("Path %s is not a directory", path)
        exit()

    return path


def main():
    if(len(sys.argv) < 2):
        print("Invalid number of arguments. Use -h or -u")
        return

    if(sys.argv[1].lower() == "-h"):
        print("This script calculates checksum of files present in the specified path")
        return

    if(sys.argv[1].lower() == "-u"):
        print("Usage : python checksum.py directoryName")
        print("directoryName : Name of the folder to be traversed.")
        return

    try:
        starttime = time.time()
        path = getValidPath(sys.argv[1])
        duplicates = findDuplicates(path)

        if(len(duplicates) == 0):
            logging.info("No duplicate files found")
            return

        printDuplicates(duplicates)
        removeDuplicates(duplicates)

        endtime = time.time()

        print("Time required to execute script is %s", (endtime - starttime))

    except ValueError:
        logging.error("Invalid datatype of input")
    except Exception as e:
        logging.error(
            "Exception while getting checksum of files from directory. ", e)


if __name__ == "__main__":
    main()
