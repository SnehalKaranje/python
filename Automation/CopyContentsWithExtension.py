import sys
import os
import shutil
from myLogging import *

myLogging.setFileName("CopyContentsWithExtension.log")
myLogging.setBasicConfig()


def copyContents(sourceDir, targetDir, fileExtension):
    if(os.path.isabs(sourceDir) == False):
        sourceDir = os.path.abspath(sourceDir)
        logging.debug("Setting absolute source directory path to " + sourceDir)

    if(os.path.isdir(sourceDir) == False):
        logging.error("Failed to find source directory " + sourceDir)
        return

    if(os.path.isabs(targetDir) == False):
        logging.debug("Setting absolute target directory path to " + targetDir)
        targetDirPath = os.path.abspath(targetDir)

    if(os.path.isdir(targetDirPath)):
        logging.error("Target directory " + targetDir +
                      " already exist. Returning")
        return

    os.mkdir(targetDir)

    for dir, subDirs, files in os.walk(sourceDir):
        for file in files:
            if(file.endswith(fileExtension)):
                logging.info("Copying file " + file +
                             " to directory " + targetDirPath)
                shutil.copy(os.path.join(dir, file), targetDirPath)


def main():
    if(len(sys.argv) < 4):
        if(len(sys.argv) == 2 and sys.argv[1].lower() == "-h"):
            print(
                "This program copies files with given extension from one directory into other")
            return
        elif(len(sys.argv) == 2 and sys.argv[1].lower() == "-u"):
            print("Please enter command in following format:")
            print("python file.py directory1 directory2 fileExtension")
            print("file.py : program to be executed")
            print("directory1 : Names of the directory from which content will be copied")
            print("directory2 : New directory in which content will be copied")
            print(
                "fileExtension : files with this extension will get copied into directory2")
            return
        else:
            print("Invalid number of arguments!")
            print("Use -h or -u.")
            return

    try:
        logging.info("Copying files with extension " +
                     sys.argv[3] + " from " + sys.argv[1] + " to " + sys.argv[2])
        copyContents(sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as e:
        logging.error("Exception while copying contents of folder " + e)


if(__name__ == "__main__"):
    main()
