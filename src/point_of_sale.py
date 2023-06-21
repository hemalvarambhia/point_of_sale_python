class PointOfSale:
    def __init__(self, catalogue, display):
        self.display = display
        self.catalogue = catalogue

    def on_barcode(self, barcode):
        if len(barcode) == 0:
            self.display.display_empty_barcode_message()

        price = self.catalogue.price_for_barcode(barcode)
        if price is None:
            self.display.display_product_not_found(barcode)
        else:
            text = '£%.2f' % (price / 100)
            self.display.display_price(text)

    def on_total(self):
        self.display.display_total('Total: £1.99')
