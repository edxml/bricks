from edxml_bricks.computing.security import SecurityBrick, CryptoBrick


def test_security_brick():
    SecurityBrick().test()


def test_crypto_brick():
    CryptoBrick().test()
