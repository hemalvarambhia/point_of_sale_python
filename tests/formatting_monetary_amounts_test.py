import unittest
import pytest
from src.display import Display


class FormattingMonetaryAmountsTest(unittest.TestCase):
    def test_amount_under_ten_pence(self):
        formatted_price = Display.formatted_price(0.02)

        self.assertEqual(formatted_price, '£0.02')

    def test_tens_of_pence(self):
        formatted_price = Display.formatted_price(0.91)

        self.assertEqual(formatted_price, '£0.91')

    def test_units_of_pounds(self):
        formatted_price = Display.formatted_price(5.00)

        self.assertEqual(formatted_price, '£5.00')

    def test_tens_of_pounds_and_some_pence(self):
        formatted_price = Display.formatted_price(20.11)

        self.assertEqual(formatted_price, '£20.11')

    def test_hundreds_of_pounds_precisely(self):
        formatted_price = Display.formatted_price(200.00)

        self.assertEqual(formatted_price, '£200.00')

    def test_hundreds_of_pounds_and_some_pence(self):
        formatted_price = Display.formatted_price(300.99)

        self.assertEqual(formatted_price, '£300.99')

    @pytest.mark.skip(reason='Test list')
    def test_thousands_of_pounds_precisely(self):
        pass

if __name__ == '__main__':
    unittest.main()
