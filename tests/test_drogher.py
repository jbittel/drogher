import drogher


class TestDrogher:
    def test_dhl_barcode(self):
        shipper = drogher.barcode('1656740256')
        assert shipper.shipper == 'DHL'

    def test_fedex_express_barcode(self):
        shipper = drogher.barcode('9632001960000000000400152152152158')
        assert shipper.shipper == 'FedEx'

    def test_fedex_ground96_barcode(self):
        shipper = drogher.barcode('9611019012345612345671')
        assert shipper.shipper == 'FedEx'

    def test_ups_barcode(self):
        shipper = drogher.barcode('1Z999AA10123456784')
        assert shipper.shipper == 'UPS'

    def test_uspsimpb_barcode(self):
        shipper = drogher.barcode('420221539101026837331000039521')
        assert shipper.shipper == 'USPS'

    def test_usps13_barcode(self):
        shipper = drogher.barcode('EF123456785US')
        assert shipper.shipper == 'USPS'

    def test_invalid_barcode(self):
        shipper = drogher.barcode('1234')
        assert shipper.shipper == 'Unknown'
