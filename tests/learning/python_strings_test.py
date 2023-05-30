import unittest
import re
import pytest


class PythonStringsTest(unittest.TestCase):
    def test_splitting_by_character(self):
        self.assertEqual(['1000', '00'], '1000.00'.split('.'))
        self.assertNotEqual([1000, 0], '1000.00'.split('.'))

    def test_reversing_a_string(self):
        self.assertEqual('0001', '1000'[::-1])

    def test_finding_all_parts_matching_a_regular_expression(self):
        matches = re.findall(r'\d{1,3}', '1000'[::-1])
        self.assertEqual(['000', '1'], matches)

    def test_joining_strings_in_an_array(self):
        joined = ','.join(['000', '1'])[::-1]
        self.assertEqual('1,000', joined)

    @pytest.mark.skip(reason = 'Test list')
    def test_joining_elements_of_an_array_into_a_string(self):
        pass


if __name__ == '__main__':
    unittest.main()
