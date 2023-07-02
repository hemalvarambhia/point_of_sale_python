import unittest
import re
import pytest


def format_monetary_amount(amount_in_pence):
    in_pounds = amount_in_pence / 100
    if amount_in_pence == 100000:
        units = '1,000'
        subunits = '00'
        return '£%s.%s' % (units, subunits)
    else:
        return '£%.2f' % in_pounds


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
