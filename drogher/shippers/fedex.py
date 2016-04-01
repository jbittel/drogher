from .base import Shipper


class FedEx(Shipper):
    barcode_pattern = r'^96\d{20}$'
    shipper = 'FedEx'

    @property
    def tracking_number(self):
        return self.barcode[7:]

    @property
    def valid_checksum(self):
        sequence, check_digit = self.tracking_number[:-1], self.tracking_number[-1]
        total = odd = even = 0
        for i, c in enumerate(reversed(sequence)):
            if i & 0x1:
                odd += int(c)
            else:
                even += int(c)
        total = (even * 3) + odd
        check = (total + (10 - total % 10)) - total
        return check == int(check_digit)
