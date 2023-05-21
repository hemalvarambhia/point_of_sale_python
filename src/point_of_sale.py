class PointOfSale:
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        self.display.set_text("£2.00")