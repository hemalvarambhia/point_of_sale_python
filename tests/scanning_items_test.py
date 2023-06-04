import unittest
from src.display import Display
from src.point_of_sale import PointOfSale
from src.catalogue import Catalogue


class ScanningItemsTest(unittest.TestCase):
    def test_when_item_is_found(self):
        display = Display()
        catalogue = Catalogue({"54321": 0.99, "12345": 2.00})
        point_of_sale = PointOfSale(display, catalogue)

        point_of_sale.on_barcode("12345")

        self.assertEqual(display.text, "£2.00", "Expected display to show £2.00 but got " + str(display))

    def test_when_any_item_is_found(self):
        display = Display()
        catalogue = Catalogue({"54321": 0.99, "12345": 2.00})
        point_of_sale = PointOfSale(display, catalogue)

        point_of_sale.on_barcode("54321")

        self.assertEqual(display.text, "£0.99", "Expected display to show £0.99 but got " + str(display))

    def test_when_item_is_not_found(self):
        display = Display()
        catalogue = Catalogue({"11111": 1.50, "77777": 12.01})
        point_of_sale = PointOfSale(display, catalogue)

        point_of_sale.on_barcode("00000")

        self.assertEqual(display.text, "Product with barcode 00000 not found")

    def test_when_any_item_is_not_found(self):
        display = Display()
        point_of_sale = PointOfSale(display, {"54321": 1.50, "09912": 12.01})

        point_of_sale.on_barcode('10011')

        self.assertEqual(display.text, 'Product with barcode 10011 not found')

    def test_no_barcode(self):
        display = Display()
        catalogue = Catalogue({"85439": 1.50, "83843": 12.01})
        point_of_sale = PointOfSale(display, catalogue)

        point_of_sale.on_barcode('')

        self.assertEqual(display.text, 'No barcode scanned')

    def test_scanning_two_items_when_both_are_found(self):
        display = Display()
        catalogue = Catalogue({'11111': 0.99, '59385': 1.00})
        point_of_sale = PointOfSale(display, catalogue)

        point_of_sale.on_barcode('11111')
        self.assertEqual(display.text, "£0.99")

        point_of_sale.on_barcode('59385')
        self.assertEqual(display.text, "£1.00")

    def test_scanning_two_items_but_only_one_is_found(self):
        display = Display()
        catalogue = Catalogue({'12311': 2.11, '98434': 0.01})
        point_of_sale = PointOfSale(display, catalogue)

        point_of_sale.on_barcode('57674')
        self.assertEqual(display.text, 'Product with barcode 57674 not found')

        point_of_sale.on_barcode('12311')
        self.assertEqual(display.text, '£2.11')

    def test_scanning_two_items_when_none_are_found(self):
        display = Display()
        catalogue = Catalogue({'12311': 2.11, '98434': 0.01})
        point_of_sale = PointOfSale(display, catalogue)

        point_of_sale.on_barcode('99999')
        self.assertEqual(display.text, 'Product with barcode 99999 not found')

        point_of_sale.on_barcode('98765')
        self.assertEqual(display.text, 'Product with barcode 98765 not found')

    def test_scanning_three_items_when_all_are_found(self):
        display = Display()
        catalogue = Catalogue({'12345': 300.00, '54321': 100.01, '55555': 10.12})
        point_of_sale = PointOfSale(display, catalogue)

        point_of_sale.on_barcode('12345')
        self.assertEqual(display.text, '£300.00')

        point_of_sale.on_barcode('54321')
        self.assertEqual(display.text, '£100.01')

        point_of_sale.on_barcode('55555')
        self.assertEqual(display.text, '£10.12')


if __name__ == '__main__':
    unittest.main()
