class PointOfSale:
    def __init__(self, display):
        self.display = display
        self.prices_by_barcode = {"54321": 0.99, "12345": 2.00}

    def on_barcode(self, barcode):
        price = self.__price_of_product_with_barcode(barcode)
        formatted_price = self.display.format_price(price)
        self.display.text = formatted_price


    def __price_of_product_with_barcode(self, barcode):
        return self.prices_by_barcode[barcode]
