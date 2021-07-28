import shutil
import sys
import os
from myLogging import *

myLogging.setFileName("CopyContents.log")
myLogging.setBasicConfig()


def copyContents(sourceDir, targetDir):
    if(os.path.isabs(sourceDir) == False):
        sourceDir = os.path.abspath(sourceDir)
        logging.debug("Setting absolute source directory path to " + sourceDir)

    if(os.path.isdir(sourceDir) == False):
        logging.error("Failed to find source directory " + sourceDir)
        return

    if(os.path.isabs(targetDir) == False):
        logging.debug("Setting absolute target directory path to " + targetDir)
        targetDir = os.path.abspath(targetDir)

    if(os.path.isdir(targetDir)):
        logging.error("Target directory " + targetDir +
                      " already exist. Returning")
        return

    # os.mkdir(targetDir);
    shutil.copytree(sourceDir, targetDir)
    logging.info("Successfully copied contents from " +
                 sourceDir + " to " + targetDir)


def main():
    if(len(sys.argv) < 3):
        if(len(sys.argv) == 2 and sys.argv[1].lower() == "-h"):
            print("This program copies contents of one directory into other")
            return
        elif(len(sys.argv) == 2 and sys.argv[1].lower() == "-u"):
            print("Please enter command in following format:")
            print("python file.py directory1 directory2")
            print("file.py : program to be executed")
            print("directory1 : Names of the directory from which content will be copied")
            print("directory2 : New directory in which content will be copied")
            return
        else:
            print("Invalid number of arguments!")
            print("Use -h or -u.")
            return

    try:
        logging.info("Copying contents from directory " +
                     sys.argv[1] + " to directory " + sys.argv[2])
        copyContents(sys.argv[1], sys.argv[2])
    except Exception as e:
        logging.error("Exception while copying contents of folder" + e)


if(__name__ == "__main__"):
    main()
