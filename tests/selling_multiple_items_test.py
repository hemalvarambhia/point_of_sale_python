import unittest
from unittest.mock import Mock
import pytest
from src.point_of_sale import PointOfSale


class SellingMultipleItemsTest(unittest.TestCase):

    def test_selling_one_item_that_is_listed_in_catalogue(self):
        display = Mock()
        catalogue = Mock()
        catalogue.configure_mock(**{'price_for_barcode.return_value': 199})
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('43512')

        point_of_sale_terminal.on_total()

        display.display_total.assert_called_with('Total: £1.99')

    def test_selling_an_item_that_is_not_listed_in_catalogue(self):
        display = Mock()
        catalogue = Mock()
        catalogue.configure_mock(**{'price_for_barcode.return_value': None})
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('55555')

        point_of_sale_terminal.on_total()

        display.display_message.assert_called_with('Nothing scanned: please try scanning a product.')

    def test_selling_two_items_both_listed_in_catalogue(self):
        display = Mock()
        catalogue = Mock()
        catalogue.price_for_barcode.side_effect = [100, 300] # 55555 costs £1 and 66666 costs £3

        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('55555')
        point_of_sale_terminal.on_barcode('66666')

        point_of_sale_terminal.on_total()

        display.display_total.assert_called_with('Total: £4.00')

    def test_selling_two_items_with_only_one_listed_in_catalogue(self):
        display = Mock()
        catalogue = Mock()
        catalogue.price_for_barcode.side_effect = [700, 799]
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('00992')
        point_of_sale_terminal.on_barcode('76543')

        point_of_sale_terminal.on_total()

        display.display_total.assert_called_with('Total: £14.99')

    def test_selling_two_items_both_not_listed_in_catalogue(self):
        display = Mock()
        catalogue = Mock()
        catalogue.price_for_barcode.side_effect = [None, None]
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('13244')
        point_of_sale_terminal.on_barcode('34444')

        point_of_sale_terminal.on_total()

        display.display_message.assert_called_with('Nothing scanned: please try scanning a product.')

    def test_selling_an_item_listed_in_catalogue_that_amounts_to_a_thousand_currency_units(self):
        display = Mock()
        catalogue = Mock()
        catalogue.configure_mock(**{'price_for_barcode.return_value': 100000})
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('00132')

        point_of_sale_terminal.on_total()

        display.display_total.assert_called_with('Total: £1,000.00')

    def test_selling_an_item_listed_in_catalogue_that_amounts_to_ten_thousand_currency_units(self):
        display = Mock()
        catalogue = Mock()
        catalogue.configure_mock(**{'price_for_barcode.return_value': 1500099})
        point_of_sale_terminal = PointOfSale(catalogue, display)
        point_of_sale_terminal.on_barcode('00132')

        point_of_sale_terminal.on_total()

        display.display_total.assert_called_with('Total: £15,000.99')

    @pytest.mark.skip(reason='Test list')
    def test_selling_an_item_listed_in_catalogue_that_amounts_to_a_hundred_thousand_currency_units(self):
        pass


if __name__ == '__main__':
    unittest.main()
