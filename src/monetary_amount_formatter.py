import re


class MonetaryAmountFormatter:
    @staticmethod
    def format_monetary_amount(amount_in_pence):
        return MonetaryAmountFormatter().format(amount_in_pence)

    def format(self, amount_in_pence):
        in_pounds = amount_in_pence / 100
        amount_as_text = '%.2f' % in_pounds
        index_of_decimal_point = amount_as_text.index('.')
        units = amount_as_text[:index_of_decimal_point]
        thousands_matcher = re.compile(r'\d{1,3}')
        decomposed = thousands_matcher.findall(''.join(reversed(units)))
        formatted_units = ''.join(reversed(','.join(decomposed)))
        subunits = amount_as_text[index_of_decimal_point + 1:]
        currency = '£'
        return '%s%s.%s' % (currency, formatted_units, subunits)
