from unittest import TestCase

from models.call_history import CallHistory


class TestCallHistory(TestCase):
    def test_load(self):
        string_input = '0987000001;0987000002;01/12/2015 04:43:33;10;352700072104120;452049C1382CF'
        result = CallHistory.load(string_input)
        self.assertEqual(result.from_phone_number, '0987000001')
