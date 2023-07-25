class Catalogue:
    def __init__(self, prices_by_barcode):
        self.prices_by_barcode = prices_by_barcode

    def price_for_barcode(self, barcode):
        return self.prices_by_barcode[barcode]