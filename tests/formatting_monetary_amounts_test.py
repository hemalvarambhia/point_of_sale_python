import unittest

import pytest


class FormattingMonetaryAmountsTest(unittest.TestCase):

    def test_formatting_amounts_under_ten_pence(self):
        self.assertEqual("£0.09", self.format_monetary_amount(9))

    @pytest.mark.skip(reason='Test list')
    def test_formatting_amounts_between_nine_pence_and_under_1_pound(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_formatting_exactly_one_pound(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_formatting_amounts_between_one_pound_and_under_one_thousand_pounds(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_formatting_exactly_one_thousand_pounds(self):
        pass

    def format_monetary_amount(self, amount_in_pence):
        in_pounds = amount_in_pence / 100
        return '£%.2f' % in_pounds
