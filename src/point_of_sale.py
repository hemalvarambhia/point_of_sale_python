class PointOfSale:
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        price = self.__price_of_product_with_barcode(barcode)
        formatted_price = PointOfSale.__format_price(price)
        self.display.text = formatted_price

    @staticmethod
    def __price_of_product_with_barcode(barcode):
        prices_by_barcode = {"54321": 0.99, "12345": 2.00}
        return prices_by_barcode[barcode]

    @staticmethod
    def __format_price(price):
        return "£" + "%0.2f" % (price)
