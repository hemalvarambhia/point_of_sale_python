import unittest
from src.display import Display
from src.point_of_sale import PointOfSale
from src.catalogue import Catalogue


class SellingItemsTest(unittest.TestCase):
    def test_selling_one_item(self):
        display = Display()
        catalogue = Catalogue({"54321": 0.99, "12345": 3.99})
        point_of_sale = PointOfSale(display, catalogue)
        point_of_sale.on_barcode("12345")

        point_of_sale.on_total()

        self.assertEqual(display.text, "Total: £3.99", "Expected display to show £3.99 but got " + str(display))

    def test_selling_one_item_and_product_is_not_found(self):
        display = Display()
        catalogue = Catalogue({"93457": 0.99, "58043": 3.99})
        point_of_sale = PointOfSale(display, catalogue)
        point_of_sale.on_barcode("99999")

        point_of_sale.on_total()

        self.assertEqual(display.text, "Nothing scanned. Please try scanning a product")

    def test_selling_two_items_when_all_are_found(self):
        display = Display()
        catalogue = Catalogue({"32323": 10.99, "84583": 2.00})
        point_of_sale = PointOfSale(display, catalogue)
        point_of_sale.on_barcode("32323")
        point_of_sale.on_barcode("84583")

        point_of_sale.on_total()

        self.assertEqual(display.text, "Total: £12.99", "Expected display to show £12.99 but got " + str(display))

    def test_scanning_two_items_items_when_only_one_is_found(self):
        display = Display()
        catalogue = Catalogue({"89999": 108.01})
        point_of_sale = PointOfSale(display, catalogue)
        point_of_sale.on_barcode("44444")
        point_of_sale.on_barcode("89999")

        point_of_sale.on_total()

        self.assertEqual(display.text, "Total: £108.01", "Expected display to show £108.01 but got " + str(display))

    def test_selling_three_items_when_none_are_found(self):
        display = Display()
        catalogue = Catalogue({"09876": 108.01})
        point_of_sale = PointOfSale(display, catalogue)
        point_of_sale.on_barcode("00000")
        point_of_sale.on_barcode("11111")
        point_of_sale.on_barcode("22222")

        point_of_sale.on_total()

        self.assertEqual(display.text, "Nothing scanned. Please try scanning a product")

    def test_selling_three_items_when_all_are_found(self):
        display = Display()
        catalogue = Catalogue({"09911": 100.01, "21199": 51.75, "31394": 100.02})
        point_of_sale = PointOfSale(display, catalogue)
        point_of_sale.on_barcode("09911")
        point_of_sale.on_barcode("21199")
        point_of_sale.on_barcode("31394")

        point_of_sale.on_total()

        self.assertEqual(display.text, 'Total: £251.78')

    def test_selling_items_totalling_thousands_of_currency_units(self):
        display = Display()
        catalogue = Catalogue({"54321": 500.01, "98765": 510.75, "00001": 100.25})
        point_of_sale = PointOfSale(display, catalogue)
        point_of_sale.on_barcode("98765")
        point_of_sale.on_barcode("00001")
        point_of_sale.on_barcode("54321")

        point_of_sale.on_total()

        self.assertEqual(display.text, 'Total: £1,111.01')


if __name__ == '__main__':
    unittest.main()
