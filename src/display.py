from src.monetary_amount_formatter import MonetaryAmountFormatter
class Display:
    def __init__(self):
        self.text = ''

    def display_price(self, price_in_pence):
        self.text = MonetaryAmountFormatter.format_monetary_amount(price_in_pence)

    def display_product_not_found(self, barcode):
        self.text = 'Product not found for barcode %s' % barcode

    def display_total(self, total_in_pence):
        formatted_monetary_amount = MonetaryAmountFormatter.format_monetary_amount(total_in_pence)
        self.text = 'Total: %s' % formatted_monetary_amount

    def display_empty_barcode_message(self):
        self.text = 'Empty barcode detected'
