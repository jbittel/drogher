Drogher
=======

A Python module implementing package tracking barcode detection and validation.

A provided barcode is tested against a list of known shipper 1D tracking barcodes, matching both the format and
checksum validity to correlate the barcode with a shipper.

Note that for some shippers the package barcode is the same as the tracking number, while for others the tracking
number is a subset of the barcode string. Inputting a tracking number instead of a barcode will work in some cases
but not in others due to this difference.

Usage
-----

Begin by importing the Drogher module::

   >>> import drogher

Now, call the barcode function with a package barcode::

   >>> package = drogher.barcode('1Z999AA10123456784')

That returns a ``Package`` subclass containing some useful information::

   >>> package.barcode
   '1Z999AA10123456784'
   >>> package.shipper
   'UPS'
   >>> package.tracking_number
   '1Z999AA10123456784'

We can also ensure the package is valid, which tells us the barcode matched an expected format and the
calculated checksum matches the check digit::

   >>> package.is_valid
   True

If a barcode cannot be matched with a shipper, the returned class will not validate::

   >>> package = drogher.barcode('123456')
   >>> package.is_valid
   False
   >>> package.shipper
   'Unknown'

For some shippers, the barcode is not the same as the tracking number::

   >>> package = drogher.barcode('420221539101026837331000039521')
   >>> package.barcode
   '420221539101026837331000039521'
   >>> package.tracking_number
   '9101026837331000039521'
   >>> package.shipper
   'USPS'
