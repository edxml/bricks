********
Contents
********

An overview of the ontology elements is provided below.

GenericBrick
============
Object types:

- boolean_
- count.big_
- count.small_
- datetime_
- datetime.duration.seconds_
- organization.name_
- organization.unit.name_
- person.name_
- sequence_
- string.generic.utf8_

Concepts:

- entity_
- entity.abstraction_
- entity.abstraction.group_
- entity.abstraction.group.social-group_
- entity.abstraction.group.social-group.organization_
- entity.abstraction.psychological-feature_
- entity.abstraction.psychological-feature.event_
- entity.abstraction.psychological-feature.event.act_
- entity.physical-entity_
- entity.physical-entity.object_
- entity.physical-entity.object.whole_
- entity.physical-entity.object.whole.living-thing_
- entity.physical-entity.object.whole.living-thing.organism_
- entity.physical-entity.object.whole.living-thing.organism.person_



***********
Definitions
***********

Object Types
============

string.generic.utf8
-------------------
*a utf-8 encoded string*

.. code-block:: xml

  <object-type name="string.generic.utf8"
               display-name-singular="string"
               display-name-plural="strings"
               description="a utf-8 encoded string"
               data-type="string:0:mc:u"
               version="1"/>

datetime
--------
*a date and time in ISO 8601 format*

.. code-block:: xml

  <object-type name="datetime"
               display-name-singular="time stamp"
               display-name-plural="time stamps"
               description="a date and time in ISO 8601 format"
               data-type="datetime"
               version="1"/>

datetime.duration.seconds
-------------------------
*an extent of time*

.. code-block:: xml

  <object-type name="datetime.duration.seconds"
               display-name-singular="time span"
               display-name-plural="time spans"
               description="an extent of time"
               data-type="number:double"
               unit-name="seconds"
               unit-symbol="s"
               prefix-radix="60"
               version="1"/>

sequence
--------
*a positive integer from a series of consecutive numbers*

.. code-block:: xml

  <object-type name="sequence"
               display-name-singular="sequence number"
               display-name-plural="sequence numbers"
               description="a positive integer from a series of consecutive numbers"
               data-type="sequence"
               version="1"/>

boolean
-------
*a boolean value (true or false)*

.. code-block:: xml

  <object-type name="boolean"
               display-name-singular="boolean value"
               display-name-plural="boolean values"
               description="a boolean value (true or false)"
               data-type="boolean"
               version="1"/>

count.small
-----------
*an integer number, representing a quantity*

.. code-block:: xml

  <object-type name="count.small"
               display-name-singular="count"
               display-name-plural="counts"
               description="an integer number, representing a quantity"
               data-type="number:smallint"
               version="1"/>

count.big
---------
*an integer number, representing a quantity*

.. code-block:: xml

  <object-type name="count.big"
               display-name-singular="count"
               display-name-plural="counts"
               description="an integer number, representing a quantity"
               data-type="number:bigint"
               version="1"/>

person.name
-----------
*a name of a person*

.. code-block:: xml

  <object-type name="person.name"
               display-name-singular="name"
               display-name-plural="names"
               description="a name of a person"
               data-type="string:0:mc:u"
               fuzzy-matching="phonetic"
               version="1"/>

organization.name
-----------------
*a name of an organized group of people with a particular purpose*

.. code-block:: xml

  <object-type name="organization.name"
               display-name-singular="organization name"
               display-name-plural="organization names"
               description="a name of an organized group of people with a particular purpose"
               data-type="string:0:mc:u"
               fuzzy-matching="phonetic"
               version="1"/>

organization.unit.name
----------------------
*a name of a specific unit within an organization*

.. code-block:: xml

  <object-type name="organization.unit.name"
               display-name-singular="unit name"
               display-name-plural="unit names"
               description="a name of a specific unit within an organization"
               data-type="string:0:mc:u"
               fuzzy-matching="phonetic"
               version="1"/>

Concepts
========

entity
------
*that which is perceived or known or inferred to have its own distinct existence*

.. code-block:: xml

  <concept name="entity"
           display-name-singular="entity"
           display-name-plural="entities"
           description="that which is perceived or known or inferred to have its own distinct existence"
           version="1"/>

entity.physical-entity
----------------------
*an entity that has physical existence*

.. code-block:: xml

  <concept name="entity.physical-entity"
           display-name-singular="physical entity"
           display-name-plural="physical entities"
           description="an entity that has physical existence"
           version="1"/>

entity.abstraction
------------------
*a concept or idea not associated with any specific instance*

.. code-block:: xml

  <concept name="entity.abstraction"
           display-name-singular="abstraction"
           display-name-plural="abstractions"
           description="a concept or idea not associated with any specific instance"
           version="1"/>

entity.physical-entity.object
-----------------------------
*a tangible and visible entity*

.. code-block:: xml

  <concept name="entity.physical-entity.object"
           display-name-singular="object"
           display-name-plural="objects"
           description="a tangible and visible entity"
           version="1"/>

entity.physical-entity.object.whole
-----------------------------------
*an assemblage of parts that is regarded as a single entity*

.. code-block:: xml

  <concept name="entity.physical-entity.object.whole"
           display-name-singular="whole"
           display-name-plural="wholes"
           description="an assemblage of parts that is regarded as a single entity"
           version="1"/>

entity.physical-entity.object.whole.living-thing
------------------------------------------------
*a living (or once living) entity*

.. code-block:: xml

  <concept name="entity.physical-entity.object.whole.living-thing"
           display-name-singular="living thing"
           display-name-plural="living things"
           description="a living (or once living) entity"
           version="1"/>

entity.physical-entity.object.whole.living-thing.organism
---------------------------------------------------------
*a living thing that has (or can develop) the ability to act or function independently*

.. code-block:: xml

  <concept name="entity.physical-entity.object.whole.living-thing.organism"
           display-name-singular="organism"
           display-name-plural="organisms"
           description="a living thing that has (or can develop) the ability to act or function independently"
           version="1"/>

entity.physical-entity.object.whole.living-thing.organism.person
----------------------------------------------------------------
*a human being*

.. code-block:: xml

  <concept name="entity.physical-entity.object.whole.living-thing.organism.person"
           display-name-singular="person"
           display-name-plural="people"
           description="a human being"
           version="1"/>

entity.abstraction.group
------------------------
*any number of entities (members) considered as a unit*

.. code-block:: xml

  <concept name="entity.abstraction.group"
           display-name-singular="group"
           display-name-plural="groups"
           description="any number of entities (members) considered as a unit"
           version="1"/>

entity.abstraction.group.social-group
-------------------------------------
*a number of people sharing some social relation*

.. code-block:: xml

  <concept name="entity.abstraction.group.social-group"
           display-name-singular="social group"
           display-name-plural="social groups"
           description="a number of people sharing some social relation"
           version="1"/>

entity.abstraction.group.social-group.organization
--------------------------------------------------
*an organized group of people working together*

.. code-block:: xml

  <concept name="entity.abstraction.group.social-group.organization"
           display-name-singular="organization"
           display-name-plural="organizations"
           description="an organized group of people working together"
           version="1"/>

entity.abstraction.psychological-feature
----------------------------------------
*a feature of the mental life of a living organism*

.. code-block:: xml

  <concept name="entity.abstraction.psychological-feature"
           display-name-singular="psychological feature"
           display-name-plural="psychological features"
           description="a feature of the mental life of a living organism"
           version="1"/>

entity.abstraction.psychological-feature.event
----------------------------------------------
*something that happens at a given place and time*

.. code-block:: xml

  <concept name="entity.abstraction.psychological-feature.event"
           display-name-singular="event"
           display-name-plural="events"
           description="something that happens at a given place and time"
           version="1"/>

entity.abstraction.psychological-feature.event.act
--------------------------------------------------
*something that people do or cause to happen*

.. code-block:: xml

  <concept name="entity.abstraction.psychological-feature.event.act"
           display-name-singular="act"
           display-name-plural="acts"
           description="something that people do or cause to happen"
           version="1"/>

