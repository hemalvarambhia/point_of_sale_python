class Display:
    def __init__(self):
        self.text = ''


    def display_price(self, price):
        formatted_price = self.format_price(price)
        self.text = formatted_price

    def format_price(self, price):
        return Display.formatted_price(price)

    @classmethod
    def formatted_price(cls, price):
        return "£" + "%0.2f" % price

    def display_product_not_found_message(self, barcode):
        self.text = 'Product with barcode %s not found' % barcode

    def display_no_barcode_message(self):
        self.text = 'No barcode scanned'

    def display_message(self, message):
        self.text = message

    def __str__(self):
        return "Display(text: " + self.text + ")"
