import re
import unittest


class PythonReLearningTest(unittest.TestCase):

    def test_reversing_a_string(self):
        self.assertEqual('0001', ''.join(reversed('1000')))

    def test_splitting_thousands_of_currency_units_after_three_zeros(self):
        regular_expression = re.compile(r'\d{1,3}')
        self.assertEqual(['000', '1'], regular_expression.findall('0001'))

    # units => pounds/dollars, subunits => pence/cents
    def test_decomposing_a_monetary_amount_into_units_and_subunits(self):
        monetary_amount = '1000.00'
        index_of_decimal_point = monetary_amount.index('.')
        pounds = monetary_amount[:index_of_decimal_point]
        pence = monetary_amount[index_of_decimal_point + 1:]
        self.assertEqual('1000', pounds)
        self.assertEqual('00', pence)

    def test_reversing_an_array(self):
        array = list(reversed(['000', '1']))

        self.assertEqual(['1', '000'], array)