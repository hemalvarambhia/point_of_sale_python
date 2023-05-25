import unittest
import pytest
from src.display import Display
from src.point_of_sale import PointOfSale


class ScanMultipleItems(unittest.TestCase):
    def test_scanning_two_items_when_both_are_found(self):
        display = Display()
        point_of_sale = PointOfSale(display, {'11111': 0.99, '59385': 1.00, '33333': 0.20})

        point_of_sale.on_barcode('11111')
        self.assertEqual(display.text, "£0.99")

        point_of_sale.on_barcode('59385')
        self.assertEqual(display.text, "£1.00")

        point_of_sale.on_barcode('33333')
        self.assertEqual(display.text, "£0.20")

    @pytest.mark.skip(reason='Test list')
    def test_scanning_two_items_but_only_one_is_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_two_items_when_none_are_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_three_items_when_all_are_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_three_items_when_all_but_one_are_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_three_items_when_only_one_is_found(self):
        pass

    def test_scanning_three_items_when_none_are_found(self):
        pass


if __name__ == '__main__':
    unittest.main()
