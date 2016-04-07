from .base import Shipper


class USPS(Shipper):
    barcode_pattern = r'^(420\d{5})?(9[1-5]\d{20,24})$'
    shipper = 'USPS'

    @property
    def tracking_number(self):
        if self.barcode.startswith('420'):
            return self.barcode[8:]
        return self.barcode

    @property
    def valid_checksum(self):
        sequence, check_digit = self.tracking_number[:-1], self.tracking_number[-1]
        odd = even = 0
        for i, c in enumerate(reversed(sequence)):
            if i & 0x1:
                odd += int(c)
            else:
                even += int(c)
        total = (even * 3) + odd
        check = (total + (10 - total % 10)) - total
        return check == int(check_digit)
