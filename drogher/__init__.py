from . import package


def barcode(b, barcode_classes=package.barcode_classes):
    for klass in barcode_classes:
        pkg = getattr(package, klass)(b)
        if pkg.is_valid:
            return pkg
    return package.Unknown(b)
