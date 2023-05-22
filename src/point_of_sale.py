class PointOfSale:
    def __init__(self, display, catalog):
        self.display = display
        self.prices_by_barcode = catalog

    def on_barcode(self, barcode):
        price = self.prices_by_barcode[barcode]
        formatted_price = self.display.format_price(price)
        self.display.text = formatted_price
