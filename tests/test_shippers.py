import drogher


class TestUPS:
    def test_barcode(self):
        ups = drogher.ups('1Z9999999999999999')
        assert ups.barcode == '1Z9999999999999999'

    def test_tracking_number(self):
        ups = drogher.ups('1Z9999999999999999')
        assert ups.tracking_number == '1Z9999999999999999'

    def test_shipper(self):
        ups = drogher.ups('1Z9999999999999999')
        assert ups.shipper == 'UPS'

    def test_is_valid(self):
        ups = drogher.ups('1Z9999999999999999')
        assert ups.is_valid == True

    def test_matches_barcode(self):
        ups = drogher.ups('1Z9999999999999999')
        assert ups.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '1A' instead of '1Z'
        ups = drogher.ups('1A9999999999999999')
        assert ups.matches_barcode == False


class TestDHL:
    def test_barcode(self):
        dhl = drogher.dhl('9999999999')
        assert dhl.barcode == '9999999999'
    
    def test_tracking_number(self):
        dhl = drogher.dhl('9999999999')
        assert dhl.tracking_number == '9999999999'

    def test_shipper(self):
        dhl = drogher.dhl('9999999999')
        assert dhl.shipper == 'DHL'

    def test_is_valid(self):
        dhl = drogher.dhl('9999999999')
        assert dhl.is_valid == True

    def test_matches_barcode(self):
        dhl = drogher.dhl('9999999999')
        assert dhl.matches_barcode == True

    def test_not_matches_barcode(self):
        # 9 digits instead of 10 digits
        dhl = drogher.dhl('999999999')
        assert dhl.matches_barcode == False


class TestFedEx:
    def test_barcode(self):
        fedex = drogher.fedex('9611019012345612345671')
        assert fedex.barcode == '9611019012345612345671'

    def test_tracking_number(self):
        fedex = drogher.fedex('9611019012345612345671')
        assert fedex.tracking_number == '012345612345671'


    def test_shipper(self):
        fedex = drogher.fedex('9611019012345612345671')
        assert fedex.shipper == 'FedEx'

    def test_is_valid(self):
        fedex = drogher.fedex('9611019012345612345671')
        assert fedex.is_valid == True

    def test_matches_barcode(self):
        fedex = drogher.fedex('9611019012345612345671')
        assert fedex.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '69' instead of '96'
        fedex = drogher.fedex('6911019012345612345671')
        assert fedex.matches_barcode == False
