from .base import Shipper


class UPS(Shipper):
    barcode_pattern = r'^1Z[A-Z0-9]{16}$'
    shipper = 'UPS'

    @property
    def valid_checksum(self):
        sequence, check_digit = self.tracking_number[2:-1], self.tracking_number[-1]
        odd = even = 0
        for i, c in enumerate(sequence):
            try:
                num = int(c)
            except ValueError:
                num = (ord(c) - 3) % 10

            if i & 0x1:
                odd += num
            else:
                even += num
        total = (odd * 2) + even
        check = (total + (10 - total % 10)) - total
        return check == int(check_digit)
