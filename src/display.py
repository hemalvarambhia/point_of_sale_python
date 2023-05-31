import re


class Display:
    def __init__(self):
        self.text = ''

    def display_price(self, price):
        formatted_price = Display.formatted_price(price)
        self.display_message(formatted_price)

    @staticmethod
    def formatted_price(price):
        formatted = "%0.2f" % price
        position_of_decimal_place = formatted.index('.')
        after_decimal_point = position_of_decimal_place + 1
        pence = formatted[after_decimal_point:]
        pound = formatted[:position_of_decimal_place]
        if price <= 999.99:
            return '£' + pound + '.' + pence
        else:
            pound_reversed = pound[::-1]
            decomposed = re.findall(r'\d{1,3}', pound_reversed)
            joined_with_comma = ','.join(decomposed[::-1])
            return '£' + joined_with_comma + '.' + pence

    def display_product_not_found_message(self, barcode):
        self.display_message('Product with barcode %s not found' % barcode)

    def display_no_barcode_message(self):
        self.display_message('No barcode scanned')

    def display_message(self, message):
        self.text = message

    def __str__(self):
        return "Display(text: " + self.text + ")"
