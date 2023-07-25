import unittest
from src.monetary_amount_formatter import MonetaryAmountFormatter


class FormattingMonetaryAmountsTest(unittest.TestCase):

    def test_formatting_amounts_under_ten_pence(self):
        self.assertEqual("£0.09", MonetaryAmountFormatter.format_monetary_amount(9))

    def test_formatting_amounts_between_nine_pence_and_under_1_pound(self):
        self.assertEqual("£0.19", MonetaryAmountFormatter.format_monetary_amount(19))

    def test_formatting_exactly_one_pound(self):
        self.assertEqual("£1.00", MonetaryAmountFormatter.format_monetary_amount(100))

    def test_formatting_amounts_between_one_pound_and_under_one_thousand_pounds(self):
        self.assertEqual("£999.00", MonetaryAmountFormatter.format_monetary_amount(99900))

    def test_formatting_exactly_one_thousand_pounds(self):
        self.assertEqual("£1,000.00", MonetaryAmountFormatter.format_monetary_amount(100000))

    def test_formatting_thousand_pounds_and_some_pence(self):
        self.assertEqual("£1,000.99", MonetaryAmountFormatter.format_monetary_amount(100099))

    def test_formatting_tens_of_thousands_pounds_exactly(self):
        self.assertEqual("£10,000.00", MonetaryAmountFormatter.format_monetary_amount(1000000))
