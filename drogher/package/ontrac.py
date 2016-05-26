from .base import Package


class OnTrac(Package):
    barcode_pattern = r'^[A-Z][0-9]{14}$'
    shipper = 'OnTrac'

    @property
    def valid_checksum(self):
        chars, check_digit = self.tracking_number[:-1], self.tracking_number[-1]
        odd = even = 0
        for i, char in enumerate(chars):
            try:
                num = int(char)
            except ValueError:
                num = (ord(char) - 3) % 10

            if i & 0x1:
                odd += num
            else:
                even += num
        check = ((odd * 2) + even) % 10
        if check != 0:
            check = 10 - check
        return check == int(check_digit)
