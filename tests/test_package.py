from drogher import package


class TestDHL:
    def test_barcode(self):
        dhl = package.DHL('1656740256')
        assert dhl.barcode == '1656740256'

    def test_barcode_spaces(self):
        dhl = package.DHL('165 674 025 6')
        assert dhl.barcode == '1656740256'

    def test_tracking_number(self):
        dhl = package.DHL('1656740256')
        assert dhl.tracking_number == '1656740256'

    def test_shipper(self):
        dhl = package.DHL('1656740256')
        assert dhl.shipper == 'DHL'

    def test_is_valid(self):
        dhl = package.DHL('1656740256')
        assert dhl.is_valid == True

    def test_matches_barcode(self):
        dhl = package.DHL('1656740256')
        assert dhl.matches_barcode == True

    def test_not_matches_barcode(self):
        # 9 digits instead of 10 digits
        dhl = package.DHL('165674025')
        assert dhl.matches_barcode == False


class TestFedExExpress:
    def test_barcode(self):
        fedex = package.FedExExpress('9632001960000000000400152152152158')
        assert fedex.barcode == '9632001960000000000400152152152158'

    def test_barcode_spaces(self):
        fedex = package.FedExExpress('9632001 960000000000 400 152152152158')
        assert fedex.barcode == '9632001960000000000400152152152158'

    def test_tracking_number(self):
        fedex = package.FedExExpress('9632001960000000000400152152152158')
        assert fedex.tracking_number == '152152152158'

    def test_tracking_number_leading_zero(self):
        fedex = package.FedExExpress('9632001960000000000400052152152158')
        assert fedex.tracking_number == '052152152158'

    def test_shipper(self):
        fedex = package.FedExExpress('9632001960000000000400152152152158')
        assert fedex.shipper == 'FedEx'

    def test_is_valid(self):
        fedex = package.FedExExpress('9632001960000000000400152152152158')
        assert fedex.is_valid == True

    def test_matches_barcode(self):
        fedex = package.FedExExpress('9632001960000000000400152152152158')
        assert fedex.matches_barcode == True

    def test_not_matches_barcode(self):
        # Contains 33 digits instead of 34
        fedex = package.FedExExpress('632001960000000000400152152152158')
        assert fedex.matches_barcode == False


class TestFedExGround96:
    def test_barcode(self):
        fedex = package.FedExGround96('9611019012345612345671')
        assert fedex.barcode == '9611019012345612345671'

    def test_barcode_spaces(self):
        fedex = package.FedExGround96('96110190 123456 123456 7 1')
        assert fedex.barcode == '9611019012345612345671'

    def test_tracking_number(self):
        fedex = package.FedExGround96('9611019012345612345671')
        assert fedex.tracking_number == '012345612345671'

    def test_shipper(self):
        fedex = package.FedExGround96('9611019012345612345671')
        assert fedex.shipper == 'FedEx'

    def test_is_valid(self):
        fedex = package.FedExGround96('9611019012345612345671')
        assert fedex.is_valid == True

    def test_valid_checksum_zero_checksum(self):
        fedex = package.FedExGround96('9611019012345612345640')
        assert fedex.valid_checksum == True

    def test_matches_barcode(self):
        fedex = package.FedExGround96('9611019012345612345671')
        assert fedex.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '69' instead of '96'
        fedex = package.FedExGround96('6911019012345612345671')
        assert fedex.matches_barcode == False


class TestOnTrac:
    def test_barcode(self):
        ontrac = package.OnTrac('C11235523929147')
        assert ontrac.barcode == 'C11235523929147'

    def test_barcode_spaces(self):
        ontrac = package.OnTrac('C 11235523929147')
        assert ontrac.barcode == 'C11235523929147'

    def test_tracking_number(self):
        ontrac = package.OnTrac('C11235523929147')
        assert ontrac.tracking_number == 'C11235523929147'

    def test_shipper(self):
        ontrac = package.OnTrac('C11235523929147')
        assert ontrac.shipper == 'OnTrac'

    def test_is_valid(self):
        ontrac = package.OnTrac('C11235523929147')
        assert ontrac.is_valid == True

    def test_valid_checksum_zero_checksum(self):
        ontrac = package.OnTrac('C11235523929840')
        assert ontrac.valid_checksum == True

    def test_matches_barcode(self):
        ontrac = package.OnTrac('D10010945303074')
        assert ontrac.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '2' instead of 'C'
        ontrac = package.OnTrac('211235523929147')
        assert ontrac.matches_barcode == False


class TestUPS:
    def test_barcode(self):
        ups = package.UPS('1Z999AA10123456784')
        assert ups.barcode == '1Z999AA10123456784'

    def test_barcode_spaces(self):
        ups = package.UPS('1Z 999 AA 10123456784')
        assert ups.barcode == '1Z999AA10123456784'

    def test_tracking_number(self):
        ups = package.UPS('1Z999AA10123456784')
        assert ups.tracking_number == '1Z999AA10123456784'

    def test_shipper(self):
        ups = package.UPS('1Z999AA10123456784')
        assert ups.shipper == 'UPS'

    def test_is_valid(self):
        ups = package.UPS('1Z999AA10123456784')
        assert ups.is_valid == True

    def test_valid_checksum_zero_checksum(self):
        ups = package.UPS('1Z879E930346834440')
        assert ups.valid_checksum == True

    def test_matches_barcode(self):
        ups = package.UPS('1Z999AA10123456784')
        assert ups.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '1A' instead of '1Z'
        ups = package.UPS('1A999AA10123456784')
        assert ups.matches_barcode == False


class TestUSPSIMpb:
    def test_barcode(self):
        usps = package.USPSIMpb('420221539101026837331000039521')
        assert usps.barcode == '420221539101026837331000039521'

    def test_barcode_spaces(self):
        usps = package.USPSIMpb('420 22153 9101026837331000039521')
        assert usps.barcode == '420221539101026837331000039521'

    def test_tracking_number(self):
        usps = package.USPSIMpb('420221539101026837331000039521')
        assert usps.tracking_number == '9101026837331000039521'

    def test_shipper(self):
        usps = package.USPSIMpb('420221539101026837331000039521')
        assert usps.shipper == 'USPS'

    def test_shipper_no_zip(self):
        usps = package.USPSIMpb('9212391234567812345670')
        assert usps.shipper == 'USPS'

    def test_is_valid(self):
        usps = package.USPSIMpb('420221539101026837331000039521')
        assert usps.is_valid == True

    def test_valid_checksum_zero_checksum(self):
        usps = package.USPSIMpb('9212391234567812345670')
        assert usps.valid_checksum == True

    def test_matches_barcode(self):
        usps = package.USPSIMpb('420221539101026837331000039521')
        assert usps.matches_barcode == True

    def test_not_matches_barcode(self):
        # Begins with '430' instead of '420'
        usps = package.USPSIMpb('430221539101026837331000039521')
        assert usps.matches_barcode == False


class TestUSPSS10:
    def test_barcode(self):
        usps = package.USPSS10('EF123456785US')
        assert usps.barcode == 'EF123456785US'

    def test_barcode_spaces(self):
        usps = package.USPSS10('EF 12345678 5 US')
        assert usps.barcode == 'EF123456785US'

    def test_tracking_number(self):
        usps = package.USPSS10('EF123456785US')
        assert usps.tracking_number == 'EF123456785US'

    def test_shipper(self):
        usps = package.USPSS10('EF123456785US')
        assert usps.shipper == 'USPS'

    def test_is_valid(self):
        usps = package.USPSS10('EF123456785US')
        assert usps.is_valid == True

    def test_valid_checksum_remainder_10(self):
        usps = package.USPSS10('RZ030057180PH')
        assert usps.valid_checksum == True

    def test_valid_checksum_remainder_11(self):
        usps = package.USPSS10('VA456789015KG')
        assert usps.valid_checksum == True

    def test_matches_barcode(self):
        usps = package.USPSS10('EF123456785US')
        assert usps.matches_barcode == True

    def test_not_matches_barcode(self):
        # Only 8 digits instead of 9
        usps = package.USPSS10('EF12345678US')
        assert usps.matches_barcode == False


class TestUnknown:
    def test_barcode(self):
        unknown = package.Unknown('ABCD')
        assert unknown.barcode == 'ABCD'

    def test_tracking_number(self):
        unknown = package.Unknown('ABCD')
        assert unknown.tracking_number == 'ABCD'

    def test_shipper(self):
        unknown = package.Unknown('ABCD')
        assert unknown.shipper is None

    def test_is_valid(self):
        unknown = package.Unknown('ABCD')
        assert unknown.is_valid == False

    def test_matches_barcode(self):
        unknown = package.Unknown('ABCD')
        assert unknown.matches_barcode == False

    def test_valid_checksum(self):
        unknown = package.Unknown('ABCD')
        assert unknown.valid_checksum == False
