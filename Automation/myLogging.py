import logging


class myLogging:
    level = logging.DEBUG
    fileName = "myLog.log"
    filemode = "a"
    format = "%(asctime)s : %(name)s : %(levelname)s : %(message)s"
    datefmt = "%m/%d/%Y %I:%M:%S %p"

    @classmethod
    def setLogLevel(cls, logLevel):
        cls.level = logLevel

    @classmethod
    def setFileName(cls, file):
        cls.fileName = file

    @classmethod
    def setFileMode(cls, filemode):
        cls.filemode = filemode

    @classmethod
    def setFileFormat(cls, fileFormat):
        cls.format = fileFormat

    @classmethod
    def setDateFormat(cls, dateFormat):
        cls.datefmt = dateFormat

    @classmethod
    def setBasicConfig(cls):
        logging.basicConfig(level=cls.level, filename=cls.fileName,
                            filemode=cls.filemode, format=cls.format, datefmt=cls.datefmt)
