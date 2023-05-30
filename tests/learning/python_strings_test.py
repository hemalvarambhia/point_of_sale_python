import unittest
import re
import pytest


class PythonStringsTest(unittest.TestCase):
    def test_reversing_a_string(self):
        self.assertEqual('0001', '1000'[::-1])

    def test_finding_all_parts_matching_a_regular_expression(self):
        reversed = '1000'[::-1]
        matches = re.findall(r'\d{1,3}', reversed)

        self.assertEqual(['000', '1'], matches)

    def test_joining_strings_in_an_array(self):
        joined = ','.join(['000', '1'])[::-1]

        self.assertEqual('1,000', joined)

    def test_we_can_format_money_in_the_thousands(self):
        reversed = '1000'[::-1]
        decomposed = re.findall(r'\d{1,3}', reversed)
        joined_with_comma = ','.join(decomposed[::-1])

        self.assertEqual('1,000', joined_with_comma)

    def test_calculating_position_of_decimal_point(self):
        position_of_decimal_point = '1000.99'.index('.', 0, -1)
        self.assertEqual(4, position_of_decimal_point)

        position_of_decimal_point = '1000000.99'.index('.', 0, -1)
        self.assertEqual(7, position_of_decimal_point)

    def test_calculating_pound_part_of_a_monetary_amount(self):
        monetary_amount = '1000.99'

        position_of_decimal_point = monetary_amount.index('.', 0, -1)
        pound_part = monetary_amount[:position_of_decimal_point]

        self.assertEqual('1000', pound_part)

    @pytest.mark.skip(reason = 'Test list')
    def test_calculating_pence_part_of_a_monetary_amount(self):
        pass



if __name__ == '__main__':
    unittest.main()
