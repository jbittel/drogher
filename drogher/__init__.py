from . import package


def barcode(b, barcode_classes=None):
    if barcode_classes is None:
        barcode_classes = ['DHL', 'FedExExpress', 'FedExGround96', 'UPS', 'USPSIMpb', 'USPSS10']
    for klass in barcode_classes:
        p = getattr(package, klass)(b)
        if p.is_valid:
            return p
    return package.Unknown(b)
