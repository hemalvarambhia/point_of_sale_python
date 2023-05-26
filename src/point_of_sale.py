class PointOfSale:
    def __init__(self, display, catalog):
        self.display = display
        self.catalogue = catalog
        self.prices_of_scanned_items = []

    def on_barcode(self, barcode):
        if barcode == '':
            self.display.display_no_barcode_message()
            return

        if barcode not in self.catalogue:
            self.display.display_product_not_found_message(barcode)
        else:
            price = self.catalogue[barcode]
            self.prices_of_scanned_items.append(price)
            self.display.display_price(price)

    def on_total(self):
        if len(self.prices_of_scanned_items) == 0:
            self.display.display_message('Nothing scanned. Please try scanning a product')
        else:
            total_price = self.prices_of_scanned_items[0]
            self.display.display_message('Total: £%0.2f' % total_price)
