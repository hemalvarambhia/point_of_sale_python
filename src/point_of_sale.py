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
        if barcode == "54321":
            return "£0.99"
        else:
            return "£2.00"