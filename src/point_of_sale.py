class PointOfSale:
    def __init__(self, display, catalog):
        self.display = display
        self.catalogue = catalog

    def on_barcode(self, barcode):
        if barcode not in self.catalogue:
            self.display.text = 'Product with barcode %s not found' % barcode
        else:
            price = self.catalogue[barcode]
            self.display.display_price(price)
