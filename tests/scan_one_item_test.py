import unittest
from unittest.mock import Mock
import pytest


class PointOfSale:
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        self.display.display_price('£1.99')


class ScanOneItemTest(unittest.TestCase):
    def test_failing_hookup(self):
        self.assertEqual(1 + 1, 2)  # add assertion here

    def test_scanning_one_item_that_is_in_catalogue(self):
        display = Mock()

        point_of_sale_terminal = PointOfSale(display)
        point_of_sale_terminal.on_barcode('12345')

        display.display_price.assert_called_with('£1.99')

    @pytest.mark.skip(reason='Test list')
    def test_scanning_one_item_that_is_not_in_catalogue(self):
        pass


if __name__ == '__main__':
    unittest.main()
