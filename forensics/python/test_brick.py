from edxml_bricks.computing.forensics import generic
from edxml_bricks.computing.forensics.platforms import windows


def test_generic_brick():
    generic.ForensicsBrick().test()


def test_windows_brick():
    windows.WindowsBrick().test()
