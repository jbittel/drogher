from .base import Shipper


class USPS(Shipper):
    shipper = 'USPS'


class USPSIMpb(USPS):
    barcode_pattern = r'^(420\d{5})?(9[1-5]\d{20,24})$'

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


class USPS13(USPS):
    barcode_pattern = r'^[A-Z]{2}\d{9}[A-Z]{2}$'

    @property
    def valid_checksum(self):
        sequence, check_digit = self.tracking_number[2:10], self.tracking_number[10]
        total = 0
        for c, d in zip(sequence, [8, 6, 4, 2, 3, 5, 9, 7]):
            total += int(c) * d
        remainder = total % 11
        if remainder == 0:
            check = 5
        elif remainder == 1:
            check = 0
        else:
            check = 11 - remainder
        return check == int(check_digit)
