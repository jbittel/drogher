import re


class Package(object):
    barcode = None
    barcode_pattern = None
    shipper = None

    def __init__(self, barcode):
        self.barcode = barcode

    def __repr__(self):
        return "%s('%s')" % ('package.' + self.__class__.__name__, self.barcode)

    @property
    def is_valid(self):
        if self.matches_barcode and self.valid_checksum:
            return True
        return False

    @property
    def matches_barcode(self):
        return bool(re.match(self.barcode_pattern, self.barcode))

    @property
    def tracking_number(self):
        return self.barcode

    @property
    def valid_checksum(self):
        return False


class Unknown(Package):
    shipper = 'Unknown'

    @property
    def matches_barcode(self):
        return False