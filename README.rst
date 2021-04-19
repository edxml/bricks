===================================
The EDXML Ontology Brick Collection
===================================

This repository contains a collection of `EDXML ontology bricks <http://www.edxml.org/bricks>`_. These bricks contain generic object types and concepts that are shared among EDXML data sources.

Data sources that make use of these bricks yield data that can be correlated automatically, yielding a single consistent body of knowledge.

An index of all object types and concepts defined in the brick collection is available `here <index.rst>`_.

Instructions for contributors can be found `here <CONTRIBUTING.rst>`_.

Contents
========

Python Packages
---------------

The repository contains a number of Python packages that are intended to be used in conjunction with the `EDXML SDK <https://github.com/edxml/sdk>`_. Importing a package will register one or more ontology bricks with the Ontology class. Each package covers a specific domain.

An overview of the Python packages is given below.

- `edxml-bricks-computing <computing/README.rst>`_
- `edxml-bricks-computing-networking <networking/README.rst>`_
- `edxml-bricks-computing-security <security/README.rst>`_
- `edxml-bricks-finance <finance/README.rst>`_
- `edxml-bricks-forensics <forensics/README.rst>`_
- `edxml-bricks-generic <generic/README.rst>`_
- `edxml-bricks-geography <geography/README.rst>`_

EDXML Serializations
--------------------

The ontology elements defined in the ontology bricks are also available as EDXML files that can be imported using any EDXML parser.
