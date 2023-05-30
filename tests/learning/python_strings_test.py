import unittest
import re
import pytest


class PythonStringsTest(unittest.TestCase):
    def test_reversing_a_string(self):
        self.assertEqual('0001', '1000'[::-1])

    def test_finding_all_parts_matching_a_regular_expression(self):
        matches = re.findall(r'\d{1,3}', '1000'[::-1])
        self.assertEqual(['000', '1'], matches)

    def test_joining_strings_in_an_array(self):
        joined = ','.join(['000', '1'])[::-1]

        self.assertEqual('1,000', joined)

if __name__ == '__main__':
    unittest.main()
