import unittest
import pytest


class FindingPricesByProductBarcodeTest(unittest.TestCase):

    @pytest.mark.skip(reason='Test list')
    def test_price_is_returned_when_barcode_is_in_catalogue(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_nothing_is_returned_when_barcode_is_not_in_catalogue(self):
        pass


if __name__ == '__main__':
    unittest.main()
