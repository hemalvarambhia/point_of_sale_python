import unittest
import pytest
from src.display import Display


class FormattingMonetaryAmountsTest(unittest.TestCase):
    def test_amount_under_ten_pence(self):

        formatted_price = Display.formatted_price(0.02)

        self.assertEqual(formatted_price, '£0.02')

    @pytest.mark.skip(reason='Test list')
    def test_tens_of_pence(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_tens_of_pounds_and_some_pence(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_pounds_and_precisely(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_hundreds_of_pounds_precisely(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_hundreds_of_pounds_and_some_pence(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_nine_hundred_and_ninety_nine_pounds_precisely(self):
        pass

    @pytest.mark.skip(reason='Test list')
    def test_thousands_of_pounds_precisely(self):
        pass

if __name__ == '__main__':
    unittest.main()
