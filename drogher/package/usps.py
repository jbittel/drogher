import re

from .base import Package


class USPS(Package):
    shipper = 'USPS'


class USPSIMpb(USPS):
    barcode_pattern = r'^(?:420(?:\d{9}|\d{5}))?(9[1-5]\d{20,24})$'

    @property
    def tracking_number(self):
        return re.match(self.barcode_pattern, self.barcode).group(1)

    @property
    def valid_checksum(self):
        chars, check_digit = self.tracking_number[:-1], self.tracking_number[-1]
        odd = even = 0
        for i, char in enumerate(reversed(chars)):
            if i & 0x1:
                odd += int(char)
            else:
                even += int(char)
        check = ((even * 3) + odd) % 10
        if check != 0:
            check = 10 - check
        return check == int(check_digit)


class USPSS10(USPS):
    barcode_pattern = r'^[A-Z]{2}\d{9}[A-Z]{2}$'

    @property
    def valid_checksum(self):
        chars, check_digit = self.tracking_number[2:10], self.tracking_number[10]
        total = 0
        for digit, char in zip([8, 6, 4, 2, 3, 5, 9, 7], chars):
            total += int(char) * digit
        check = 11 - (total % 11)
        if check == 10:
            check = 0
        elif check == 11:
            check = 5
        return check == int(check_digit)


class USPS20(USPS):
    barcode_pattern = r'^(71|73|77|81)\d{18}$'

    @property
    def valid_checksum(self):
        chars, check_digit = self.tracking_number[:-1], self.tracking_number[-1]
        odd = even = 0
        for i, char in enumerate(reversed(chars)):
            if i & 0x1:
                odd += int(char)
            else:
                even += int(char)
        check = ((even * 3) + odd) % 10
        if check != 0:
            check = 10 - check
        return check == int(check_digit)
