import unittest
import pytest
from src.display import Display
from src.point_of_sale import PointOfSale


class SellOneItemTest(unittest.TestCase):
    def test_sell_one_item_when_item_is_found(self):
        display = Display()
        point_of_sale = PointOfSale(display, {"54321": 0.99, "12345": 2.00})

        point_of_sale.on_barcode("12345")

        self.assertEqual(display.text, "£2.00", "Expected display to show £2.00 but got " + str(display))

    def test_sell_any_one_item_when_item_is_found(self):
        display = Display()
        point_of_sale = PointOfSale(display, {"54321": 0.99, "12345": 2.00})

        point_of_sale.on_barcode("54321")

        self.assertEqual(display.text, "£0.99", "Expected display to show £0.99 but got " + str(display))

    @pytest.mark.skip(reason = "Test list")
    def test_sell_one_item_when_item_is_not_found(self):
        display = Display()
        point_of_sale = PointOfSale(display, {"11111": 1.50, "77777": 12.01})

        point_of_sale.on_barcode("00000")

        self.assertEqual(display.text, "Product with barcode 00000 not found")

    @pytest.mark.skip(reason = "Test list")
    def test_no_barcode(self):
        pass


if __name__ == '__main__':
    unittest.main()
