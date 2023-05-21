import unittest
import pytest


class SellOneItemTest(unittest.TestCase):
    def test_failing_hookup(self):
        self.assertEqual(1 + 1, 2)

    @pytest.mark.skip(reason = "Test list")
    def test_sell_one_item_when_item_is_found(self):
        self.assertEqual(display.text, "£2.00")

    @pytest.mark.skip(reason = "Test list")
    def test_sell_one_item_when_item_is_not_found(self):
        pass


if __name__ == '__main__':
    unittest.main()
