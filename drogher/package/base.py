import re


class Package(object):
    barcode = ''
    barcode_pattern = ''
    shipper = ''

    def __init__(self, barcode):
        self.barcode = barcode.replace(' ', '')

    def __repr__(self):
        return "%s('%s')" % ('package.' + self.__class__.__name__, self.barcode)

    @property
    def is_valid(self):
        if self.matches_barcode and self.valid_checksum:
            return True
        return False

    @property
    def matches_barcode(self):
        if self.barcode_pattern and self.barcode:
            return bool(re.match(self.barcode_pattern, self.barcode))
        return False

    @property
    def tracking_number(self):
        return self.barcode

    @property
    def valid_checksum(self):
        return False


class Unknown(Package):
    shipper = None
