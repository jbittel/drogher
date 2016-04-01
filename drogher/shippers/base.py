import re


class Shipper(object):
    barcode = None
    barcode_pattern = None
    shipper = 'Unknown'

    def __init__(self, barcode):
        self.barcode = barcode

    @property
    def is_valid(self):
        if not self.matches_barcode or not self.valid_checksum:
            return False
        return True

    @property
    def matches_barcode(self):
        return bool(re.match(self.barcode_pattern, self.barcode))

    @property
    def tracking_number(self):
        return self.barcode

    @property
    def valid_checksum(self):
        return True
