class PointOfSale:
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        if barcode == "54321":
            self.display.set_text("£0.99")
        else:
            self.display.set_text("£2.00")