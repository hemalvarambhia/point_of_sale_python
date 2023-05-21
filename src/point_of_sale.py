class PointOfSale:
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        price = self.__price_of_product_with_barcode(barcode)
        self.display.text = price

    @staticmethod
    def __price_of_product_with_barcode(barcode):
        prices_by_barcode = {"54321": 0.99, "12345": 2.00}
        return "£" + "%0.2f" % (prices_by_barcode[barcode])
