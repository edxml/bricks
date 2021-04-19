from edxml_bricks.finance.currencies.all import AllCurrenciesBrick
from edxml_bricks.finance.currencies.common import CommonCurrenciesBrick
from edxml_bricks.finance.generic import FinanceBrick


def test_finance_brick():
    FinanceBrick().test()


def test_all_currencies_brick():
    AllCurrenciesBrick().test()


def test_common_currencies_brick():
    CommonCurrenciesBrick().test()
