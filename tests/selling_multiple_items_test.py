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

    @pytest.mark.skip(reason='Test list')
    def test_selling_an_item_that_is_not_listed_in_catalogue(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_two_items_both_listed_in_catalogue(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_two_items_with_only_one_listed_in_catalogue(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_two_items_both_not_listed_in_catalogue(self):
        pass


if __name__ == '__main__':
    unittest.main()
