import sys
import os
import time
import psutil
import urllib.request as urllib
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def is_connected():
    try:
        urllib.urlopen("https://www.google.com", timeout=1)
        return True
    except Exception:
        return False


def sendProcessDetails(file):
    try:
        fromaddr = "snehalkaranje298@gmail.com"
        toaddr = "snehalkaranje9@gmail.com"
        body = "PFA, process details"

        attachment = open(file, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename=%s" % file)

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Process details"
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(p)

        text = msg.as_string()

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "**********")
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

        print("Log file successfully sent through mail")

    except Exception as e:
        print("Exception while sending mail", e)


def getProcessesDetails(path):
    fptr = open(path, "w")
    try:
        for process in psutil.process_iter():
            pInfo = process.as_dict(attrs=["name", "pid", "username"])
            fptr.write(str(pInfo))
            fptr.write("\n")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

    fptr.close()


def getLogFilePath(path):
    if not os.path.isdir(path):
        print("directory " + path + " does not exist")
        exit()

    return os.path.join(path, "log%s.txt" % (time.ctime()))


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

    path = getLogFilePath(sys.argv[1])
    getProcessesDetails(path)
    if is_connected():
        sendProcessDetails(path)
    else:
        print("No internet connection")


if __name__ == "__main__":
    main()
