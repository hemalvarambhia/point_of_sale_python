import unittest
import pytest


class ScanMultipleItems(unittest.TestCase):
    @pytest.mark.skip(reason='Test list')
    def test_scanning_two_items_when_both_are_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_two_items_but_only_one_is_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_two_items_when_none_are_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_three_items_when_all_are_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_three_items_when_all_but_one_are_found(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_scanning_three_items_when_only_one_is_found(self):
        pass

    def test_scanning_three_items_when_none_are_found(self):
        pass


if __name__ == '__main__':
    unittest.main()
