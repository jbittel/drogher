import drogher


class TestDrogher:
    def test_dhl_barcode(self):
        package = drogher.barcode('1656740256')
        assert package.shipper == 'DHL'

    def test_fedex_express_barcode(self):
        package = drogher.barcode('9632001960000000000400152152152158')
        assert package.shipper == 'FedEx'

    def test_fedex_ground96_barcode(self):
        package = drogher.barcode('9611019012345612345671')
        assert package.shipper == 'FedEx'

    def test_ontrac_barcode(self):
        package = drogher.barcode('D10010945303074')
        assert package.shipper == 'OnTrac'

    def test_ups_barcode(self):
        package = drogher.barcode('1Z999AA10123456784')
        assert package.shipper == 'UPS'

    def test_uspsimpb_barcode(self):
        package = drogher.barcode('420221539101026837331000039521')
        assert package.shipper == 'USPS'

    def test_uspss10_barcode(self):
        package = drogher.barcode('EF123456785US')
        assert package.shipper == 'USPS'

    def test_invalid_barcode(self):
        package = drogher.barcode('1234')
        assert package.shipper is None

    def test_barcode_classes(self):
        package = drogher.barcode('EF123456785US', barcode_classes=['DHL'])
        assert package.shipper is None
        package = drogher.barcode('1656740256', barcode_classes=['DHL'])
        assert package.shipper == 'DHL'
