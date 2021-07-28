import sys
import os
import checksum
from myLogging import *

myLogging.setFileName("ChecksumLog.txt")
myLogging.setBasicConfig()


def displayChecksum(path):
    for dirName, subDirs, files in os.walk(path):
        logging.debug("Current directory is : %s", dirName)
        for file in files:
            filePath = os.path.join(dirName, file)
            fileHash = checksum.hashfile(filePath)
            logging.info("File : %s checksum : %s", file, fileHash)


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
        path = getValidPath(sys.argv[1])
        displayChecksum(path)
    except ValueError:
        logging.error("Invalid datatype of input")
    except Exception:
        logging.error(
            "Exception while getting checksum of files from directory. " + e)


if __name__ == "__main__":
    main()
