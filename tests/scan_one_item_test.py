import unittest
import pytest

class ScanOneItemTest(unittest.TestCase):
    def test_failing_hookup(self):
        self.assertEqual(1 + 1, 2)  # add assertion here

    @pytest.mark.skip(reason = 'Test list')
    def test_scanning_one_item_that_is_in_catalogue(self):
        pass

    @pytest.mark.skip(reason = 'Test list')
    def test_scanning_one_item_that_is_not_in_catalogue(self):
        pass


if __name__ == '__main__':
    unittest.main()
