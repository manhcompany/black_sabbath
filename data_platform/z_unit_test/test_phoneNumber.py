from unittest import TestCase

from models.phone_number import PhoneNumber


class TestPhoneNumber(TestCase):
    def test_load(self):
        input_str = "0987000001,2016-03-01,2016-05-01"
        phone_number = PhoneNumber.load(input_str)
        self.assertIsNotNone(phone_number)
        self.assertEqual(phone_number.phone_number, "0987000001")
        self.assertEqual(phone_number.activation_date, ["2016-03-01"])
        self.assertEqual(phone_number.deactivation_date, ["2016-05-01"])

        input_str_not_deactivation_date = "0987000002,2016-05-01,"
        phone_number_not_deactivation_date = PhoneNumber.load(input_str_not_deactivation_date)
        self.assertIsNotNone(phone_number_not_deactivation_date)
        self.assertEqual(phone_number_not_deactivation_date.phone_number, "0987000002")
        self.assertEqual(phone_number_not_deactivation_date.activation_date, ["2016-05-01"])
        self.assertEqual(phone_number_not_deactivation_date.deactivation_date, [])

    def test_add(self):
        a_input_str = "0987000001,2016-03-01,2016-05-01"
        b_input_str = "0987000001,2016-09-01,2016-12-01"
        phone_number_a = PhoneNumber.load(a_input_str)
        phone_number_b = PhoneNumber.load(b_input_str)
        phone_number_added = PhoneNumber.add(phone_number_a, phone_number_b)
        self.assertIsNotNone(phone_number_added)
        self.assertEqual(phone_number_added.activation_date, ["2016-03-01", "2016-09-01"])
        self.assertEqual(phone_number_added.deactivation_date, ["2016-05-01", "2016-12-01"])

    def test_transform(self):
        input_str = "0987000001,2016-03-01,2016-05-01"
        phone_number = PhoneNumber.load(input_str)
        self.assertEqual(phone_number, phone_number.transform())

    def test_get_str(self):
        input_str = "0987000001,2016-03-01,2016-05-01"
        phone_number = PhoneNumber.load(input_str)
        phone_number.actual_activation_date = "2016-05-01"
        self.assertEqual(phone_number.get_str(), "0987000001,2016-05-01")

    def test_find_actual_activation(self):
        input_str = "0987000001,2016-03-01,2016-05-01"
        phone_number = PhoneNumber.load(input_str)
        phone_number.activation_date.append("2016-01-01")
        phone_number.activation_date.append("2016-12-01")
        phone_number.activation_date.append("2016-09-01")
        phone_number.activation_date.append("2016-06-01")
        phone_number.deactivation_date.append("2016-03-01")
        phone_number.deactivation_date.append("2016-12-01")
        phone_number.deactivation_date.append("2016-09-01")
        phone_number.find_actual_activation()
        self.assertEqual(phone_number.actual_activation_date, "2016-06-01")
