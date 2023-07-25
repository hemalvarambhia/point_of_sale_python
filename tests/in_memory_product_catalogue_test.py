import unittest
from src.catalogue import Catalogue


class InMemoryProductCatalogueTest(unittest.TestCase):

    def test_finding_price_of_product_listed_in_catalogue(self):
        catalogue = Catalogue({'12345': 199})
        self.assertEqual(199, catalogue.price_for_barcode('12345'))

    def test_finding_price_of_any_product_listed_in_catalogue(self):
        catalogue = Catalogue({'98765': 30000})
        self.assertEqual(30000, catalogue.price_for_barcode('98765'))

    def test_finding_no_price_when_product_is_not_in_catalogue(self):
        catalogue = Catalogue({'65789': 30000})

        self.assertEqual(None, catalogue.price_for_barcode('11111'))
