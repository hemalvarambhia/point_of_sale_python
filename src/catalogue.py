class Catalogue:

    def __init__(self, catalogue):
        self.catalogue = catalogue

    def __getitem__(self, barcode):
        if barcode in self.catalogue:
            return self.catalogue[barcode]
        else:
            return None
