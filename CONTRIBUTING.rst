=================
How to contribute
=================

Thanks for considering contributing to the EDXML ontology brick collection.

Submitting new definitions
==========================
When contributing a new definition please consider the following:

- Only definitions that are likely to be shared by multiple EDXML data sources should be submitted. Definitions that are specific to a particular data source should be kept with that data source.
- Make sure that your definition is clear. For example, an object type definition must not leave any room for doubt about what kind of values belong to its value space and which do not.
- Make sure that your definition does not give rise to any confusion when comparing it to other existing definitions. The use case for each object type or concept must be clear and clearly distinguished from others.
- Take upgrade options into consideration. Some attributes can be changed after initial publication, others cannot. Please consult `the EDXML specification <http://edxml.org/>`_ for details. Generally, it is better to be on the strict side and optionally loosen the definition in later versions.
- Concept names should be composed using the hypernym / hyponym relations from the Princeton WordNet lexicon. A convenient interface for browsing the WordNet lexicon is `English WordNet <https://en-word.net/>`_.
- Descriptions of object types and concepts should include a leading non-particular article ("a" or "an").

Submitting changes to existing definitions
==========================================
When contributing a change to an existing definition please do not remove any code in the definition. In stead, append changes and end your changes using a call to the ``upgrade()`` method. For example, consider the following existing object type definition:

.. code-block:: python

    yield target_ontology.create_object_type(cls.OBJECT_SHA1)\
        .set_description('a SHA-1 hash')\
        .set_data_type(DataType.hex(length=20))\
        .set_display_name('SHA1 hash', 'SHA1 hashes')\
        .set_version(1)

Now, in order to change the description, append the following method calls:

.. code-block:: python

    yield target_ontology.create_object_type(cls.OBJECT_SHA1)\
        .set_description('a SHA-1 hash') \
        .set_data_type(DataType.hex(length=20))\
        .set_display_name('SHA1 hash', 'SHA1 hashes')\
        .set_version(1)\
        .set_description('a SHA-1 cryptographic hash')\
        .upgrade()

The call to ``upgrade()`` will do two things. First, it will verify if the changes that were applied since the last call to either ``set_version()`` or ``upgrade()`` are backward compatible. Backward incompatible changes will result in failing unit tests. Second, it will increment the version of the ontology element.
