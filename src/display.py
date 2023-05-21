class Display:

    def set_text(self, text):
        self.text = "£2.00"

    def __str__(self):
        return "Display(text: " + self.text +")"