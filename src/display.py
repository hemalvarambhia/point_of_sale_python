import re
class Display:
    def __init__(self):
        self.text = ''

    def display_price(self, price):
        formatted_price = Display.formatted_price(price)
        self.display_message(formatted_price)

    @staticmethod
    def formatted_price(price):
        if price <= 999.99:
            return "£" + "%0.2f" % price
        else:
            formatted = "%0.2f" % price
            after_decimal_point = formatted.index('.') + 1
            pence = formatted[after_decimal_point:]
            reversed = '1000'[::-1]
            decomposed = re.findall(r'\d{1,3}', reversed)
            joined_with_comma = ','.join(decomposed[::-1])
            return '£' +joined_with_comma + '.' + pence

    def display_product_not_found_message(self, barcode):
        self.display_message('Product with barcode %s not found' % barcode)

    def display_no_barcode_message(self):
        self.display_message('No barcode scanned')

    def display_message(self, message):
        self.text = message

    def __str__(self):
        return "Display(text: " + self.text + ")"
