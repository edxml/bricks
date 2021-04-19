from edxml_bricks.computing.networking import generic, http


def test_generic_brick():
    generic.NetworkingBrick().test()


def test_http_brick():
    http.HttpBrick().test()
