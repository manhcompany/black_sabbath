from unittest import TestCase
from utils.converter import StringConverter


class TestStringConverter(TestCase):
    def test_convert_string2timestamp(self):
        input_str = '2017-12-22'
        output = StringConverter.convert_string2timestamp(input_str)
        print(output)
        self.assertEqual(first=output, second=1513875600.0)

    def test_convert_datetime2string(self):
        timestamp = 1513875600.0
        output = StringConverter.convert_timestamp2string(-2.0)
        print(output)
        output = StringConverter.convert_timestamp2string(timestamp)

        self.assertEqual(first=output, second='2017-12-22')
