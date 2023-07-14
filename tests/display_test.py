import unittest
import pytest
from src.monetary_amount_formatter import MonetaryAmountFormatter


class Display:
    def __init__(self):
        self.text = ''

    def display_price(self, price_in_pence):
        self.text = MonetaryAmountFormatter.format_monetary_amount(price_in_pence)


class DisplayTest(unittest.TestCase):

    def test_displaying_a_price_that_is_pence_only(self):
        display = Display()

        display.display_price(5)

        self.assertEqual('£0.05', display.text)

    def test_displaying_a_price_that_is_pounds_only(self):
        display = Display()

        display.display_price(1200)

        self.assertEqual('£12.00', display.text)

    @pytest.mark.skip(reason='Test list')
    def test_displaying_a_price_that_is_pounds_and_pence(self):
        pass

    def test_displaying_a_price_that_is_thousands_pounds_exactly(self):
        display = Display()

        display.display_price(100000)

        self.assertEqual('£1,000.00', display.text)

    def test_displaying_a_price_that_is_hundreds_of_thousands_pounds_exactly(self):
        display = Display()

        display.display_price(10000000)

        self.assertEqual('£100,000.00', display.text)

    def test_displaying_a_price_that_is_millions_of_pounds_exactly(self):
        display = Display()

        display.display_price(100000000)

        self.assertEqual('£1,000,000.00', display.text)

    def test_displaying_monetary_amounts_formatted_in_the_western_system(self):
        amounts_and_formats = {
            5: '£0.05',
            199: '£1.99',
            1200: '£12.00',
            112010: '£1,120.10',
            10000091: '£100,000.91',
            100000100: '£1,000,001.00'
        }

        display = Display()
        for amount, expected_format in amounts_and_formats.items():

            display.display_price(amount)

            self.assertEqual(expected_format, display.text)