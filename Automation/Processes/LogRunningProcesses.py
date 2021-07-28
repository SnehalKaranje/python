import sys
import os
import psutil


def getProcessesDetails(path):
    fptr = open(os.path.join(path, "log.txt"), "w")
    try:
        for process in psutil.process_iter():
            pInfo = process.as_dict(attrs=["name", "pid", "username"])
            fptr.write(str(pInfo))
            fptr.write("\n")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

    fptr.close()


def getValidPath(path):
    if not os.path.isdir(path):
        print("directory " + path + " does not exist")
        exit()

    return path


def main():
    if(len(sys.argv) < 2):
        print("Invlid arguments! Use -h or -u")
        return
    if(len(sys.argv) == 2 and sys.argv[1].lower() == "-h"):
        print("This program generates a log file with details of the running processes in the directory provided by the user.")
        return
    if(len(sys.argv) == 2 and sys.argv[1].lower() == "-u"):
        print("Usage: python processInfo.py directory")
        return

    path = getValidPath(sys.argv[1])
    getProcessesDetails(path)


if __name__ == "__main__":
    main()
