import re


class MonetaryAmountFormatter:
    @staticmethod
    def format_monetary_amount(amount_in_pence):
        return MonetaryAmountFormatter('£').format(amount_in_pence)

    def __init__(self, currency):
        self.currency = currency

    def format(self, amount_in_subunits):
        in_currency_units = amount_in_subunits / 100
        amount_as_text = '%.2f' % in_currency_units
        index_of_decimal_point = amount_as_text.index('.')
        units = amount_as_text[:index_of_decimal_point]
        thousands_matcher = re.compile(r'\d{1,3}')
        decomposed = thousands_matcher.findall(''.join(reversed(units)))
        formatted_units = ''.join(reversed(','.join(decomposed)))
        subunits = amount_as_text[index_of_decimal_point + 1:]
        return '%s%s.%s' % (self.currency, formatted_units, subunits)
