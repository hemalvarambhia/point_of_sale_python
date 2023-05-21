class PointOfSale:
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        if barcode == "54321":
            price = "£0.99"
        else:
            price = "£2.00"

        self.display.text = price