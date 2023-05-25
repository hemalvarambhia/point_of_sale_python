import unittest
import pytest


class SellingItemsTest(unittest.TestCase):
    @pytest.mark.skip(reason='Test list')
    def test_selling_one_item(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_one_item_and_product_is_not_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_two_items_when_all_are_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_two_items_items_when_only_one_is_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_selling_three_items_when_none_are_found(self):
        pass


if __name__ == '__main__':
    unittest.main()
