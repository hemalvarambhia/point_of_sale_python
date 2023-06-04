import unittest
from src.catalogue import Catalogue


class FindingPricesByProductBarcodeTest(unittest.TestCase):

    def test_price_is_returned_when_barcode_is_in_catalogue(self):
        catalog = Catalogue({'12345': 50, '54321': 25, '11111': 2})

        self.assertEqual(catalog['12345'], 50)

    def test_price_is_return_for_any_barcode_in_catalogue(self):
        catalog = Catalogue({'12345': 50, '55555': 12})

        self.assertEqual(catalog['55555'], 12)

    def test_nothing_is_returned_when_barcode_is_not_in_catalogue(self):
        catalog = Catalogue({'88888': 11, '22222': 190})

        self.assertEqual(catalog['99999'], None)


if __name__ == '__main__':
    unittest.main()
