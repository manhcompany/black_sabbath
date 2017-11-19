import decimal
import simplejson
import time
import datetime

class DecimalJSONEncoder(simplejson.JSONEncoder):

    def default(self, o):
        """
        convert decimal type for elasticsearch
        :param o:
        :type o:
        :return:
        :rtype:
        """
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)


class DictVerify:
    @staticmethod
    def get(dictionary, default, keys):
        """
        get value from dictionary by chain of keys
        :param dictionary: dictionary
        :type dictionary: dict
        :param default: default value if keys not exist in dictionary
        :type default: object
        :param keys: chain of keys
        :type keys: list
        :return: value of key
        :rtype: object
        """
        temp = dictionary
        for i in keys:
            if i in temp:
                temp = temp[i]
            else:
                return default
        if temp is None:
            return default
        return temp


class StringConverter:
    """
    String converter
    """
    @staticmethod
    def convert_string2timestamp(str):
        """
        Convert string to timestamp
        :param str: str
        :return: float
        """
        return time.mktime(datetime.datetime.strptime(str, "%Y-%m-%d").timetuple())

    @staticmethod
    def convert_timestamp2string(timestamp):
        """
        Convert timestamp to string
        :param timestamp: float
        :return: string Y-m-d
        """
        if timestamp >= 0.0:
            return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        else:
            return None
