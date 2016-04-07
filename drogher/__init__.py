from . import shippers


def barcode(b):
    for klass in ['DHL', 'FedExExpress', 'FedExGround', 'UPS', 'USPS']:
        shipper = getattr(shippers, klass)(b)
        if shipper.is_valid:
            return shipper
    return shippers.Unknown(b)
