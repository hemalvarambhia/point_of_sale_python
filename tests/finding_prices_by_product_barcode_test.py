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

    def test_we_can_confirm_a_product_is_in_the_catalogue(self):
        catalogue = Catalogue({'11111': 11, '55555': 190})

        predicate = '55555' in catalogue

        self.assertEqual(predicate, True)

    def test_we_can_confirm_a_product_is_not_in_the_catalogue(self):
        catalogue = Catalogue({'43989': 199, '94595': 1899})

        not_in_catalogue = '00000' not in catalogue

        self.assertEqual(not_in_catalogue, True)


if __name__ == '__main__':
    unittest.main()
