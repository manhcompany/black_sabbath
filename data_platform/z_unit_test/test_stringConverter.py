from unittest import TestCase
from utils.converter import StringConverter


class TestStringConverter(TestCase):
    def test_convert_string2timestamp(self):
        input_str = '2017-12-22'
        output = StringConverter.convert_string2timestamp(input_str)
        print(output)
        self.assertEqual(first=output, second=1513875600.0)

    def test_convert_string2timestamp_00(self):
        input_str = '01/12/2015 04:43:33'
        output = StringConverter.convert_string2timestamp(input_str, "%d/%m/%Y %H:%M:%S")
        print(output)
        self.assertEqual(first=output, second=1448919813.0)

    def test_convert_datetime2string(self):
        timestamp = 1513875600.0
        output = StringConverter.convert_timestamp2string(-2.0)
        print(output)
        output = StringConverter.convert_timestamp2string(timestamp)

        self.assertEqual(first=output, second='2017-12-22')

    def test_convert_datetime2string_00(self):
        timestamp = 1448919813.0
        output = StringConverter.convert_timestamp2string(timestamp, "%d/%m/%Y %H:%M:%S")
        print(output)
        self.assertEqual(first=output, second='01/12/2015 04:43:33')

    def test_convert_string2timestamp_01(self):
        input_str = '04:43:33'
        output = StringConverter.convert_string2timestamp(input_str, "%H:%M:%S")
        print(output)
        self.assertEqual(first=output, second=-2208997387.0)