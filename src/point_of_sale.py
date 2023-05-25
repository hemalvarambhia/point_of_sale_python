class PointOfSale:
    def __init__(self, display, catalog):
        self.display = display
        self.catalogue = catalog

    def on_barcode(self, barcode):
        if barcode == '':
            self.display.text = 'No barcode scanned'
            return

        if barcode not in self.catalogue:
            self.display.display_product_not_found_message(barcode)
        else:
            price = self.catalogue[barcode]
            self.display.display_price(price)
