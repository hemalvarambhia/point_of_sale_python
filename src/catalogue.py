class Catalogue:

    def __init__(self, catalogue):
        self.catalogue = catalogue

    def __getitem__(self, barcode):
        return self.catalogue.get(barcode, None)