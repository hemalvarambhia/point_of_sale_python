import unittest
from unittest.mock import Mock
import pytest


class PointOfSale:
    def __init__(self, catalogue, display):
        self.display = display
        self.catalogue = catalogue

    def on_barcode(self, barcode):
        price = self.catalogue.price_for_barcode(barcode)
        if price is None:
            self.display.display_product_not_found(barcode)
        else:
            text = '£%.2f' % (price / 100)
            self.display.display_price(text)


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

    @pytest.mark.skip(reason='Test list')
    def test_scanning_empty_barcode(self):
        display = Mock()
        catalogue = Mock()
        catalogue.configure_mock(**{'price_for_barcode.return_value': 1299})
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('')

        display.display_empty_barcode_message.assert_called()


if __name__ == '__main__':
    unittest.main()
