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

    def test_valid_checksum_zero_checksum(self):
        ups = shippers.UPS('1Z879E930346834440')
        assert ups.valid_checksum == True

    def test_matches_barcode(self):
        ups = shippers.UPS('1Z999AA10123456784')
        assert ups.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '1A' instead of '1Z'
        ups = shippers.UPS('1A999AA10123456784')
        assert ups.matches_barcode == False


class TestUSPSIMpb:
    def test_barcode(self):
        usps = shippers.USPSIMpb('420221539101026837331000039521')
        assert usps.barcode == '420221539101026837331000039521'

    def test_tracking_number(self):
        usps = shippers.USPSIMpb('420221539101026837331000039521')
        assert usps.tracking_number == '9101026837331000039521'

    def test_shipper(self):
        usps = shippers.USPSIMpb('420221539101026837331000039521')
        assert usps.shipper == 'USPS'

    def test_shipper_no_zip(self):
        usps = shippers.USPSIMpb('9212391234567812345670')
        assert usps.shipper == 'USPS'

    def test_is_valid(self):
        usps = shippers.USPSIMpb('420221539101026837331000039521')
        assert usps.is_valid == True

    def test_valid_checksum_zero_checksum(self):
        usps = shippers.USPSIMpb('9212391234567812345670')
        assert usps.valid_checksum == True

    def test_matches_barcode(self):
        usps = shippers.USPSIMpb('420221539101026837331000039521')
        assert usps.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '430' instead of '420'
        usps = shippers.USPSIMpb('430221539101026837331000039521')
        assert usps.matches_barcode == False


class TestUSPS13:
    def test_barcode(self):
        usps = shippers.USPS13('EF123456785US')
        assert usps.barcode == 'EF123456785US'

    def test_tracking_number(self):
        usps = shippers.USPS13('EF123456785US')
        assert usps.tracking_number == 'EF123456785US'

    def test_shipper(self):
        usps = shippers.USPS13('EF123456785US')
        assert usps.shipper == 'USPS'

    def test_is_valid(self):
        usps = shippers.USPS13('EF123456785US')
        assert usps.is_valid == True

    def test_matches_barcode(self):
        usps = shippers.USPS13('EF123456785US')
        assert usps.matches_barcode == True

    def test_not_matches_barcode(self):
        # Only 8 digits instead of 9
        usps = shippers.USPS13('EF12345678US')
        assert usps.matches_barcode == False


class TestUnknown:
    def test_barcode(self):
        unknown = shippers.Unknown('ABCD')
        assert unknown.barcode == 'ABCD'

    def test_tracking_number(self):
        unknown = shippers.Unknown('ABCD')
        assert unknown.tracking_number == 'ABCD'

    def test_shipper(self):
        unknown = shippers.Unknown('ABCD')
        assert unknown.shipper == 'Unknown'

    def test_is_valid(self):
        unknown = shippers.Unknown('ABCD')
        assert unknown.is_valid == False

    def test_matches_barcode(self):
        unknown = shippers.Unknown('ABCD')
        assert unknown.matches_barcode == False
