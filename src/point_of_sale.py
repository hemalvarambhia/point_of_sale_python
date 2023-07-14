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
            self.display.display_price(price)

    def on_total(self):
        if len(self.prices_of_items_scanned) == 0:
            self.display.display_message('Nothing scanned: please try scanning a product.')
        else:
            total_price = sum(self.prices_of_items_scanned)
            self.display.display_total(total_price)

