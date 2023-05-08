import logging
import os

# C
class Logger():

    def __init__(self):
        self.logPath = "log/"

    def log(self, logClass: str, error: str) -> None:

        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)   

        logging.basicConfig(
                level    = logging.INFO,
                filename = "log/" + logClass + "_errors.log",
                filemode = "a",
                format   = "%(asctime)s %(levelname)s %(message)s"
            )
        logging.error(error) 
        print(error)
