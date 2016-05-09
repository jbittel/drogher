drogher
=======

Identify shippers and valid tracking numbers from package barcodes.

A package barcode string is tested against known shipper barcode types, matching the format and calculating
checksum validity to identify the type provided. The module supports these barcode formats:

   * DHL
   * FedEx Express
   * FedEx Ground "96"
   * OnTrac
   * UPS
   * USPS IMpb
   * USPS UPU S10

**Note:** For some shippers the package barcode is the same as the tracking number, while for others the tracking
number is a subset of the barcode. Inputting a tracking number instead of a barcode will work in some cases but
not others.

Usage
-----

Begin by importing the Drogher module::

   >>> import drogher

Now, call the ``barcode`` function with a package barcode string::

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

If a barcode cannot be matched with a shipper, the class does not validate and the shipper is ``None``::

   >>> package = drogher.barcode('123456')
   >>> package.is_valid
   False
   >>> package.shipper
   None

For some shippers, the barcode is not the same as the tracking number::

   >>> package = drogher.barcode('420221539101026837331000039521')
   >>> package.barcode
   '420221539101026837331000039521'
   >>> package.tracking_number
   '9101026837331000039521'
   >>> package.shipper
   'USPS'
