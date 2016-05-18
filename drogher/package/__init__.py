from .base import Unknown
from .dhl import DHL
from .fedex import FedExExpress
from .fedex import FedExGround96
from .ontrac import OnTrac
from .ups import UPS
from .usps import USPSIMpb
from .usps import USPSS10


barcode_classes = ['DHL', 'FedExExpress', 'FedExGround96', 'OnTrac', 'UPS', 'USPSIMpb', 'USPSS10']
