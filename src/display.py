class Display:
    def __init__(self):
        self.text = ''


    def display_price(self, price):
        formatted_price = self.format_price(price)
        self.text = formatted_price

    def format_price(self, price):
        return "£" + "%0.2f" % price

    def display_product_not_found_message(self, barcode):
        self.text = 'Product with barcode %s not found' % barcode

    def __str__(self):
        return "Display(text: " + self.text + ")"
