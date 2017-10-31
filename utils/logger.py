import logging
import logging.config
import json
import os


class Logger(object):
    def __init__(self, class_name):
        """
        constructor
        :param class_name: name of class
        :type class_name: str
        """
        with open(os.environ['LOGGER_CONFIG']) as f:
            c = json.loads(f.read())

        logging.config.dictConfig(c)
        self.logger = logging.getLogger(class_name)

    def get(self):
        """
        get Logger
        :return: logger
        :rtype: Logger
        """
        return self.logger
