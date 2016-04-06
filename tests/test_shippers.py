from drogher import shippers


class TestDHL:
    def test_barcode(self):
        dhl = shippers.DHL('1656740256')
        assert dhl.barcode == '1656740256'

    def test_tracking_number(self):
        dhl = shippers.DHL('1656740256')
        assert dhl.tracking_number == '1656740256'

    def test_shipper(self):
        dhl = shippers.DHL('1656740256')
        assert dhl.shipper == 'DHL'

    def test_is_valid(self):
        dhl = shippers.DHL('1656740256')
        assert dhl.is_valid == True

    def test_matches_barcode(self):
        dhl = shippers.DHL('1656740256')
        assert dhl.matches_barcode == True

    def test_not_matches_barcode(self):
        # 9 digits instead of 10 digits
        dhl = shippers.DHL('165674025')
        assert dhl.matches_barcode == False


class TestFedExExpress:
    def test_barcode(self):
        fedex = shippers.FedExExpress('9632001960000000000400152152152158')
        assert fedex.barcode == '9632001960000000000400152152152158'

    def test_tracking_number(self):
        fedex = shippers.FedExExpress('9632001960000000000400152152152158')
        assert fedex.tracking_number == '152152152158'

    def test_shipper(self):
        fedex = shippers.FedExExpress('9632001960000000000400152152152158')
        assert fedex.shipper == 'FedEx'

    def test_is_valid(self):
        fedex = shippers.FedExExpress('9632001960000000000400152152152158')
        assert fedex.is_valid == True

    def test_matches_barcode(self):
        fedex = shippers.FedExExpress('9632001960000000000400152152152158')
        assert fedex.matches_barcode == True

    def test_not_matches_barcode(self):
        # Contains 33 digits instead of 34
        fedex = shippers.FedExExpress('632001960000000000400152152152158')
        assert fedex.matches_barcode == False


class TestFedExGround:
    def test_barcode(self):
        fedex = shippers.FedExGround('9611019012345612345671')
        assert fedex.barcode == '9611019012345612345671'

    def test_tracking_number(self):
        fedex = shippers.FedExGround('9611019012345612345671')
        assert fedex.tracking_number == '012345612345671'

    def test_shipper(self):
        fedex = shippers.FedExGround('9611019012345612345671')
        assert fedex.shipper == 'FedEx'

    def test_is_valid(self):
        fedex = shippers.FedExGround('9611019012345612345671')
        assert fedex.is_valid == True

    def test_matches_barcode(self):
        fedex = shippers.FedExGround('9611019012345612345671')
        assert fedex.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '69' instead of '96'
        fedex = shippers.FedExGround('6911019012345612345671')
        assert fedex.matches_barcode == False


class TestUPS:
    def test_barcode(self):
        ups = shippers.UPS('1Z999AA10123456784')
        assert ups.barcode == '1Z999AA10123456784'

    def test_tracking_number(self):
        ups = shippers.UPS('1Z999AA10123456784')
        assert ups.tracking_number == '1Z999AA10123456784'

    def test_shipper(self):
        ups = shippers.UPS('1Z999AA10123456784')
        assert ups.shipper == 'UPS'

    def test_is_valid(self):
        ups = shippers.UPS('1Z999AA10123456784')
        assert ups.is_valid == True

    def test_matches_barcode(self):
        ups = shippers.UPS('1Z999AA10123456784')
        assert ups.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '1A' instead of '1Z'
        ups = shippers.UPS('1A999AA10123456784')
        assert ups.matches_barcode == False
