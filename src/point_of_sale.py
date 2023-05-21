class PointOfSale:
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        if barcode == "54321":
            self.display.text ="£0.99"
        else:
            self.display.text = "£2.00"