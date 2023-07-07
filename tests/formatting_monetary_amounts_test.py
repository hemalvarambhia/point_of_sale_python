import unittest
import re


def format_monetary_amount(amount_in_pence):
    in_pounds = amount_in_pence / 100
    amount_as_text = '%.2f' % in_pounds
    index_of_decimal_point = amount_as_text.index('.')
    units = amount_as_text[:index_of_decimal_point]
    thousands_matcher = re.compile(r'\d{1,3}')
    decomposed = thousands_matcher.findall(''.join(reversed(units)))
    units = ''.join(reversed(','.join(decomposed)))
    subunits = amount_as_text[index_of_decimal_point + 1:]
    return '£%s.%s' % (units, subunits)


class FormattingMonetaryAmountsTest(unittest.TestCase):

    def test_formatting_amounts_under_ten_pence(self):
        self.assertEqual("£0.09", format_monetary_amount(9))

    def test_formatting_amounts_between_nine_pence_and_under_1_pound(self):
        self.assertEqual("£0.19", format_monetary_amount(19))

    def test_formatting_exactly_one_pound(self):
        self.assertEqual("£1.00", format_monetary_amount(100))

    def test_formatting_amounts_between_one_pound_and_under_one_thousand_pounds(self):
        self.assertEqual("£999.00", format_monetary_amount(99900))

    def test_formatting_exactly_one_thousand_pounds(self):
        self.assertEqual("£1,000.00", format_monetary_amount(100000))

    def test_formatting_thousand_pounds_and_some_pence(self):
        self.assertEqual("£1,000.99", format_monetary_amount(100099))

    def test_formatting_tens_of_thousands_pounds_exactly(self):
        self.assertEqual("£10,000.00", format_monetary_amount(1000000))
