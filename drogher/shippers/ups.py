from .base import Shipper


class UPS(Shipper):
    barcode_pattern = r'^1Z[A-Z0-9]{16}$'
    shipper = 'UPS'
