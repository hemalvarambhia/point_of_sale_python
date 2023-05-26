import unittest
import pytest
from src.display import Display
from src.point_of_sale import PointOfSale


class SellingItemsTest(unittest.TestCase):
    def test_selling_one_item(self):
        display = Display()
        point_of_sale = PointOfSale(display, {"54321": 0.99, "12345": 3.99})

        point_of_sale.on_barcode("12345")

        point_of_sale.on_total()

        self.assertEqual(display.text, "Total: £3.99", "Expected display to show £3.99 but got " + str(display))

    def test_selling_one_item_and_product_is_not_found(self):
        display = Display()
        point_of_sale = PointOfSale(display, {"93457": 0.99, "58043": 3.99})

        point_of_sale.on_barcode("99999")

        point_of_sale.on_total()

        self.assertEqual(display.text, "Nothing scanned. Please try scanning a product")

    def test_selling_two_items_when_all_are_found(self):
        display = Display()
        point_of_sale = PointOfSale(display, {"32323": 10.99, "84583": 2.00})

        point_of_sale.on_barcode("32323")
        point_of_sale.on_barcode("84583")

        point_of_sale.on_total()

        self.assertEqual(display.text, "Total: £12.99", "Expected display to show £12.99 but got " + str(display))

    @pytest.mark.skip(reason='Test list')
    def test_scanning_two_items_items_when_only_one_is_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_three_items_when_none_are_found(self):
        pass


if __name__ == '__main__':
    unittest.main()
