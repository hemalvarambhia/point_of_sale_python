import unittest

import pytest

from src.display import Display


class DisplayTest(unittest.TestCase):

    def test_displaying_monetary_amounts_formatted_in_the_western_system(self):
        amounts_and_expected_formats = {
            5: '£0.05',
            199: '£1.99',
            1200: '£12.00',
            112010: '£1,120.10',
            10000091: '£100,000.91',
            100000100: '£1,000,001.00',
            120056789: '£1,200,567.89'
        }

        display = Display()
        for amount, expected_format in amounts_and_expected_formats.items():
            display.display_price(amount)

            self.assertEqual(expected_format, display.text)

    @pytest.mark.skip(reason='Test list')
    def test_displaying_total_monetary_amounts_formatted_in_the_western_system(self):
        pass