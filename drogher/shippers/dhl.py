from .base import Shipper


class DHL(Shipper):
    barcode_pattern = r'^\d{10}$'
    shipper = 'DHL'

    @property
    def valid_checksum(self):
        chars, check_digit = self.tracking_number[:-1], self.tracking_number[-1]
        return int(chars) % 7 == int(check_digit)
