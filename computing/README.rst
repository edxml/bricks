###############
Computing Brick
###############

This directory contains `EDXML bricks <http://www.edxml.org/bricks>`_ defining ontology elements related to computer science.

An overview of included definitions can be found `here <index.rst>`_.

********************
EDXML Serializations
********************

The definitions are available as EDXML files that can be imported using any EDXML parser:

- `computing.edxml <computing.edxml>`_
- `files.edxml <files.edxml>`_
- `email.edxml <email.edxml>`_

**************
Python Package
**************

The ``python`` directory contains a Python package that is intended to be used in conjunction with the `EDXML SDK <https://github.com/edxml/sdk>`_. Importing the package will register the ontology bricks with the Ontology class.

Installing::

  pip install edxml-bricks-computing
