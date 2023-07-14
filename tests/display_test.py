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
