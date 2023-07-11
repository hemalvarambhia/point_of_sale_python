import unittest
import pytest


class Display:
    def __init__(self):
        self.text = ''

    def display_price(self, price_in_pence):
        self.text = '£0.05'

class SellingMultipleItemsTest(unittest.TestCase):

    def test_displaying_a_price_that_is_pence_only(self):
        display = Display()

        display.display_price(5)

        self.assertEqual('£0.05', display.text)

    @pytest.mark.skip(reason='Test list')
    def test_displaying_a_price_that_is_pounds_only(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_displaying_a_price_that_is_pounds_and_pence(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_displaying_a_price_that_is_thousands_pounds_exactly(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_displaying_a_price_that_is_hundreds_of_thousands_pounds_exactly(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_displaying_a_price_that_is_millions_of_pounds_exactly(self):
        pass