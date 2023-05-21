class PointOfSale:
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        if barcode == "54321":
            price = self.__price_for_barcode(barcode)
        else:
            price = self.__price_for_barcode(barcode)

        self.display.text = price

    def __price_for_barcode(self, barcode):
        prices_by_barcode = { '54321': 0.99, '12345': 2.00 }
        return '£' + '%0.2f' % (prices_by_barcode[barcode])