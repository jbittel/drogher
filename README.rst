Drogher
=======

A Python module implementing package barcode detection and validation.

Note that for some shippers the package barcode is the same as the tracking number, while for others the tracking
number is a subset of the barcode string. Inputting a tracking number instead of a barcode will work in some cases
but not in others due to this difference.

Usage
-----

Basic usage::

   >>> import drogher
   >>> package = drogher.barcode('1Z999AA10123456784')
   >>> package.shipper
   'UPS'
   >>> package.tracking_number
   '1Z999AA10123456784'
   >>> package.is_valid
   True
   >>> package = drogher.barcode('420221539101026837331000039521')
   >>> package.shipper
   'USPS'
   >>> package.tracking_number
   '9101026837331000039521'

If an unknown barcode is provided, the returned class will not validate::

   >>> package = drogher.barcode('123456')
   >>> package.shipper
   'Unknown'
   >>> package.is_valid
   False

Barcode
~~~~~~~

::

   drogher.barcode(b)

Detect and validate a barcode string.

Returns a class containing a number of useful methods.

.. method:: Package.barcode

   Returns the originally provided barcode string.

.. method:: Package.is_valid

   Returns ``True`` if the barcode is valid, ``False`` otherwise. Validity checks that the barcode matches the
   expected format and the checksum matches the check digit. An invalid package indicates it was unable to be
   matched with a configured shipper.

.. method:: Package.shipper

   Returns a string containing the name of the shipper (e.g. 'UPS', 'FedEx'). If the shipper cannot be determined,
   this returns 'Unknown'.

.. method:: Package.tracking_number

   Returns the tracking number for the package. In some cases this will be identical to the package barcode, while
   in others it will be a substring of the barcode.
