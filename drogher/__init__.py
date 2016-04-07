from . import shippers
from .exceptions import InvalidBarcode


def barcode(b):
    for klass in ['DHL', 'FedExExpress', 'FedExGround', 'UPS', 'USPS']:
        shipper = getattr(shippers, klass)(b)
        if shipper.is_valid:
            return shipper
    raise InvalidBarcode("%s is not a valid barcode" % b)
