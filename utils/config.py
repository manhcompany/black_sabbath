import json

from utils.logger import Logger


class Config:

    def __init__(self, filename):
        """
        Constructor
        :param filename: file config
        :type filename: str
        """
        self.__logger = Logger(self.__class__.__name__).get()
        self.filename = filename
        try:
            with open(self.filename) as f:
                self.data = f.read()
        except FileNotFoundError as e:
            self.__logger.error(e)
        except Exception as e:
            raise e

    def get_config(self):
        """
        get config dictionary
        :return: dictionary of config
        :rtype: dict
        """
        return json.loads(self.data)
