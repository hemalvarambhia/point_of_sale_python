import unittest
import re


class PythonStringsTest(unittest.TestCase):
    def test_splitting_by_character(self):
        self.assertEqual(['1000', '00'], '1000.00'.split('.'))
        self.assertNotEqual([1000, 0], '1000.00'.split('.'))

    def test_searching_for_all_parts_matching_regular_expression(self):
        matches = re.findall(r'\d{1,3}', '0001')
        self.assertEqual(['000', '1'], matches)


if __name__ == '__main__':
    unittest.main()
