import unittest


class SellOneItemTest(unittest.TestCase):
    def test_failing_hookup(self):
        self.assertEqual(1 + 1, 3)  # add assertion here


if __name__ == '__main__':
    unittest.main()
