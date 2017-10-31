import decimal
import simplejson
import json


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
