import unittest
import pytest


class InMemoryProductCatalogueTest(unittest.TestCase):

    @pytest.mark.skip(reason='Test list')
    def test_product_listed_in_catalogue(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_product_missing_from_catalogue(self):
        pass
