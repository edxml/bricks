from edxml_bricks.computing import generic, email, files


def test_generic_brick():
    generic.ComputingBrick().test()


def test_email_brick():
    email.EmailBrick().test()


def test_files_brick():
    files.FilesBrick().test()
