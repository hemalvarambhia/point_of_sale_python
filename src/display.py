class Display:
    def format_price(self, price):
        return "£" + "%0.2f" % price
    def __str__(self):
        return "Display(text: " + self.text + ")"
