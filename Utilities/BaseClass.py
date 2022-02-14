import inspect
import logging

import pytest as pytest


@pytest.mark.usefixtures("setup")
class BaseClass:



    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    # def capture_screenshot(self,name):
    #     self.driver.get_screenshot_as_file(name)


