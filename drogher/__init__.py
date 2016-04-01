from . import shippers
from .exceptions import InvalidBarcode


def barcode(b):
    for klass in ['DHL', 'UPS']:
        shipper = getattr(shippers, klass)(b)
        if shipper.is_valid:
            return shipper
    raise InvalidBarcode("%s is not a valid barcode" % b)


def dhl(barcode):
    return shippers.DHL(barcode)


def fedex(barcode):
    return shippers.FedEx(barcode)


def ups(barcode):
    return shippers.UPS(barcode)
