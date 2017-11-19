import hashlib


class SHA256Encoder:

    @staticmethod
    def hash(input_string):
        """
        hash input_string by SHA256
        :param input_string:
        :type input_string: str
        :return: hash
        :rtype: str
        """
        hash_object = hashlib.sha256(input_string.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig

    @staticmethod
    def verify(hash_string, input_string):
        """
        compare hash_string with input_string
        :param hash_string: hash string
        :type hash_string: str
        :param input_string: input_string, not hash
        :type input_string: str
        :return: if hash of input_string equals hash_string then return true, else return false
        :rtype: bool
        """
        hash_object = hashlib.sha256(input_string)
        hex_dig = hash_object.hexdigest()
        return hash_string == hex_dig
