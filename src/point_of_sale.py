class PointOfSale:
    def __init__(self, display, catalog):
        self.display = display
        self.prices_by_barcode = catalog

    def on_barcode(self, barcode):
        price = self.prices_by_barcode[barcode]
        self.display.display_price(price)
