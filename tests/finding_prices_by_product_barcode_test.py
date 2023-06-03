import unittest
import pytest


class Catalogue:

    def __init__(self, catalogue):
        pass

    def __getitem__(self, barcode):
        return 50



class FindingPricesByProductBarcodeTest(unittest.TestCase):

    def test_price_is_returned_when_barcode_is_in_catalogue(self):
        catalog = Catalogue({'12345': 50, '54321': 25, '11111': 2})

        self.assertEqual(catalog['12345'], 50)

    @pytest.mark.skip(reason='Test list')
    def test_nothing_is_returned_when_barcode_is_not_in_catalogue(self):
        pass


if __name__ == '__main__':
    unittest.main()
