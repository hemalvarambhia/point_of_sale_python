import unittest
from unittest.mock import Mock

import pytest

from src.point_of_sale import PointOfSale


class ScanOneItemTest(unittest.TestCase):

    def test_scanning_one_item_that_is_in_catalogue(self):
        display = Mock()
        catalogue = Mock()
        catalogue.configure_mock(**{'price_for_barcode.return_value': 199})
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('12345')

        display.display_price.assert_called_with('£1.99')

    def test_scanning_one_item_that_is_not_in_catalogue(self):
        display = Mock()
        catalogue = Mock()
        catalogue.configure_mock(**{'price_for_barcode.return_value': None})
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('56344')

        display.display_product_not_found.assert_called_with('56344')

    def test_scanning_empty_barcode(self):
        display = Mock()
        catalogue = Mock()
        catalogue.configure_mock(**{'price_for_barcode.return_value': 1299})
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('')

        display.display_empty_barcode_message.assert_called()

    def test_scan_an_item_worth_thousands_of_currency_units(self):
        display = Mock()
        catalogue = Mock()
        catalogue.configure_mock(**{'price_for_barcode.return_value': 100000})
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('')

        display.display_price.assert_called_with('£1,000.00')


if __name__ == '__main__':
    unittest.main()
