import pytest

import drogher
from drogher.exceptions import InvalidBarcode


class TestDrogher:
    def test_barcode(self):
        shipper = drogher.barcode('1Z999AA10123456784')
        assert shipper.shipper == 'UPS'

    def test_invalid_barcode(self):
        with pytest.raises(InvalidBarcode):
            drogher.barcode('1234')
