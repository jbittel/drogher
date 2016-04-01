from .base import Shipper


class DHL(Shipper):
    barcode_pattern = r'^\d{10}$'
    shipper = 'DHL'
