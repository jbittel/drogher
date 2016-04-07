from .base import Shipper


class FedEx(Shipper):
    shipper = 'FedEx'


class FedExExpress(FedEx):
    barcode_pattern = r'^\d{34}$'

    @property
    def tracking_number(self):
        return self.barcode[20:].lstrip('0')

    @property
    def valid_checksum(self):
        sequence, check_digit = self.tracking_number[:-1], self.tracking_number[-1]
        total = 0
        for c, d in zip(reversed(sequence), [1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3]):
            total += int(c) * d
        return total % 11 % 10 == int(check_digit)


class FedExGround(FedEx):
    barcode_pattern = r'^96\d{20}$'

    @property
    def tracking_number(self):
        return self.barcode[7:]

    @property
    def valid_checksum(self):
        sequence, check_digit = self.tracking_number[:-1], self.tracking_number[-1]
        odd = even = 0
        for i, c in enumerate(reversed(sequence)):
            if i & 0x1:
                odd += int(c)
            else:
                even += int(c)
        check = ((even * 3) + odd) % 10
        if check != 0:
            check = 10 - check
        return check == int(check_digit)
