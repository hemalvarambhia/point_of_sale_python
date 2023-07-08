import re
from src.monetary_amount_formatter import MonetaryAmountFormatter

class PointOfSale:
    def __init__(self, catalogue, display):
        self.display = display
        self.catalogue = catalogue
        self.prices_of_items_scanned = []

    def on_barcode(self, barcode):
        if len(barcode) == 0:
            self.display.display_empty_barcode_message()

        price = self.catalogue.price_for_barcode(barcode)
        if price is None:
            self.display.display_product_not_found(barcode)
        else:
            self.prices_of_items_scanned.append(price)
            text = '£%.2f' % (price / 100)
            self.display.display_price(text)

    def on_total(self):
        if len(self.prices_of_items_scanned) == 0:
            self.display.display_message('Nothing scanned: please try scanning a product.')
        else:
            total_price = sum(self.prices_of_items_scanned)
            formatted, pence = self.__formatted(total_price)
            total = MonetaryAmountFormatter.format_monetary_amount(total_price)
            self.display.display_total('Total: %s' % total)

    def __formatted(self, total_price):
        text = '%.2f' % (total_price / 100)
        decimal_point = text.index('.')
        thousands_units_pattern = re.compile(r'\d{1,3}')
        reversed_pounds = ''.join(reversed(text[:decimal_point]))
        pence = text[decimal_point + 1:]
        formatted = ','.join(thousands_units_pattern.findall(reversed_pounds))
        return ''.join(reversed(formatted)), pence
