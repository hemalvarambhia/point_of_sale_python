import unittest
import pytest

class SellingMultipleItemsTest(unittest.TestCase):

    @pytest.mark.skip(reason='Test list')
    def test_selling_one_item_that_is_listed_in_catalogue(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_an_item_that_is_not_listed_in_catalogue(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_two_items_both_listed_in_catalogue(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_two_items_with_only_one_listed_in_catalogue(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_two_items_both_not_listed_in_catalogue(self):
        pass


if __name__ == '__main__':
    unittest.main()
