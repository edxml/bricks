#!/usr/bin/env python3

from computing.python.edxml_bricks.computing.generic import ComputingBrick
from computing.python.edxml_bricks.computing.email import EmailBrick
from computing.python.edxml_bricks.computing.files import FilesBrick
from finance.python.edxml_bricks.finance.generic import FinanceBrick
from finance.python.edxml_bricks.finance.currencies.common import CommonCurrenciesBrick
from finance.python.edxml_bricks.finance.currencies.all import AllCurrenciesBrick
from forensics.python.edxml_bricks.computing.forensics.generic import ForensicsBrick
from forensics.python.edxml_bricks.computing.forensics.platforms.windows import WindowsBrick
from generic.python.edxml_bricks.generic import GenericBrick
from geography.python.edxml_bricks.geography import GeoBrick
from networking.python.edxml_bricks.computing.networking.generic import NetworkingBrick
from networking.python.edxml_bricks.computing.networking.http import HttpBrick
from security.python.edxml_bricks.computing.security import SecurityBrick
from security.python.edxml_bricks.computing.security import CryptoBrick

open('computing/computing.edxml', 'wb').write(ComputingBrick.as_xml())
open('computing/email.edxml', 'wb').write(EmailBrick.as_xml())
open('computing/files.edxml', 'wb').write(FilesBrick.as_xml())
open('finance/finance.edxml', 'wb').write(FinanceBrick.as_xml())
open('finance/currencies-common.edxml', 'wb').write(CommonCurrenciesBrick.as_xml())
open('finance/currencies-all.edxml', 'wb').write(AllCurrenciesBrick.as_xml())
open('forensics/forensics.edxml', 'wb').write(ForensicsBrick.as_xml())
open('forensics/windows.edxml', 'wb').write(WindowsBrick.as_xml())
open('generic/generic.edxml', 'wb').write(GenericBrick.as_xml())
open('geography/geography.edxml', 'wb').write(GeoBrick.as_xml())
open('networking/networking.edxml', 'wb').write(NetworkingBrick.as_xml())
open('networking/http.edxml', 'wb').write(HttpBrick.as_xml())
open('security/security.edxml', 'wb').write(SecurityBrick.as_xml())
open('security/crypto.edxml', 'wb').write(CryptoBrick.as_xml())
