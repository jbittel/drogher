from . import shippers


def barcode(b, barcode_classes=None):
    if barcode_classes is None:
        barcode_classes = ['DHL', 'FedExExpress', 'FedExGround96', 'UPS', 'USPSIMpb', 'USPS13']
    for klass in barcode_classes:
        shipper = getattr(shippers, klass)(b)
        if shipper.is_valid:
            return shipper
    return shippers.Unknown(b)
