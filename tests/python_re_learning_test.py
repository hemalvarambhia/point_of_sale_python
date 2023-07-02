import re
import unittest


class PythonReLearningTest(unittest.TestCase):

    def test_splitting_thousands_after_three_zeros(self):
        regular_expression = re.compile(r'\d{1,3}')
        self.assertEqual(['000', '1'], regular_expression.findall('0001'))

    def test_reversing_a_string(self):
        self.assertEqual('0001', ''.join(reversed('1000')))