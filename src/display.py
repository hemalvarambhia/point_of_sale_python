class Display:

    def set_text(self, text):
        self.text = text

    def __str__(self):
        return "Display(text: " + self.text +")"