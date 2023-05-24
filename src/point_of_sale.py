class PointOfSale:
    def __init__(self, display, catalog):
        self.display = display
        self.prices_by_barcode = catalog

    def on_barcode(self, barcode):
        if barcode not in self.prices_by_barcode:
            self.display.text = 'Product with barcode %s not found' % barcode
        else:
            price = self.prices_by_barcode[barcode]
            self.display.display_price(price)
