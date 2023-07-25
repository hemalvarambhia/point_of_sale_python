import unittest
from src.catalogue import Catalogue


class InMemoryProductCatalogueTest(unittest.TestCase):

    def test_finding_price_of_product_listed_in_catalogue(self):
        catalogue = Catalogue({'12345': 199})
        self.assertEqual(199, catalogue.price_for_barcode('12345'))

    @unittest.skip('Test list')
    def test_finding_no_price_when_product_is_not_in_catalogue(self):
        pass
