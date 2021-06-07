********
Contents
********

An overview of the ontology elements is provided below.

ComputingBrick
==============
Object types:

- computing.identifier.uuid_
- computing.identifier.oid_
- computing.data.size.bytes_
- computing.user.name_
- computing.software.product.name_
- computing.hardware.product.name_
- computing.software.product.version_
- computing.software.os.name_
- computing.cpe.uri_

Concepts:

- entity.physical-entity.object.whole.artifact.instrumentality.device.machine.computer_
- entity.physical-entity.object.whole.living-thing.organism.person.user_

EmailBrick
==========
Object types:

- computing.email.address_

FilesBrick
==========
Object types:

- computing.file.name_
- computing.file.name.ci_
- computing.file.path_
- computing.file.path.ci_

Concepts:

- entity.abstraction.communication.indication.evidence.record.file_



***********
Definitions
***********

Object Types
============

computing.identifier.uuid
-------------------------
*a universally unique identifier*

.. code-block:: xml

  <object-type name="computing.identifier.uuid"
               display-name-singular="UUID"
               display-name-plural="UUIDs"
               description="a universally unique identifier"
               data-type="uuid"
               xref="https://en.wikipedia.org/wiki/Universally_unique_identifier"
               version="1"/>

computing.identifier.oid
------------------------
*an object identifier (OID) as standardized by the International Telecommunications Union*

.. code-block:: xml

  <object-type name="computing.identifier.oid"
               display-name-singular="OID"
               display-name-plural="OIDs"
               description="an object identifier (OID) as standardized by the International Telecommunications Union"
               data-type="string:255:lc"
               xref="https://en.wikipedia.org/wiki/Object_identifier"
               regex-hard="[0-2]\.[\d]+(.\d+)*"
               version="1"/>

computing.data.size.bytes
-------------------------
*an amount of data measured in bytes*

.. code-block:: xml

  <object-type name="computing.data.size.bytes"
               display-name-singular="size"
               display-name-plural="sizes"
               description="an amount of data measured in bytes"
               data-type="number:bigint"
               unit-name="Byte"
               unit-symbol="B"
               prefix-radix="2"
               version="1"/>

computing.user.name
-------------------
*a name of a computer user account*

.. code-block:: xml

  <object-type name="computing.user.name"
               display-name-singular="user name"
               display-name-plural="user names"
               description="a name of a computer user account"
               data-type="string:255:mc:u"
               version="1"/>

computing.software.product.name
-------------------------------
*a name of a computer program*

.. code-block:: xml

  <object-type name="computing.software.product.name"
               display-name-singular="software product"
               display-name-plural="software products"
               description="a name of a computer program"
               data-type="string:255:lc:u"
               compress="true"
               fuzzy-matching="phonetic"
               version="1"/>

computing.hardware.product.name
-------------------------------
*a name of a computer system or computer component*

.. code-block:: xml

  <object-type name="computing.hardware.product.name"
               display-name-singular="hardware product"
               display-name-plural="hardware products"
               description="a name of a computer system or computer component"
               data-type="string:255:mc:u"
               compress="true"
               fuzzy-matching="phonetic"
               version="1"/>

computing.software.product.version
----------------------------------
*a version of a computer program*

.. code-block:: xml

  <object-type name="computing.software.product.version"
               display-name-singular="software version"
               display-name-plural="software versions"
               description="a version of a computer program"
               data-type="string:255:lc:u"
               compress="true"
               version="1"/>

computing.software.os.name
--------------------------
*a name of a computer operating system*

.. code-block:: xml

  <object-type name="computing.software.os.name"
               display-name-singular="operating system"
               display-name-plural="operating systems"
               description="a name of a computer operating system"
               data-type="string:255:lc:u"
               version="1"/>

computing.cpe.uri
-----------------
*a Common Platform Enumeration (CPE) URI*

.. code-block:: xml

  <object-type name="computing.cpe.uri"
               display-name-singular="CPE URI"
               display-name-plural="CPE URIs"
               description="a Common Platform Enumeration (CPE) URI"
               data-type="uri::"
               xref="https://en.wikipedia.org/wiki/Common_Platform_Enumeration"
               compress="true"
               version="1"/>

computing.email.address
-----------------------
*an RFC 5322 e-mail address*

.. code-block:: xml

  <object-type name="computing.email.address"
               display-name-singular="e-mail address"
               display-name-plural="e-mail addresses"
               description="an RFC 5322 e-mail address"
               data-type="string:254:mc:u"
               regex-soft="[\S]+@[\S]+\.[a-z]+"
               version="1"/>

computing.file.name
-------------------
*a name of a computer file*

.. code-block:: xml

  <object-type name="computing.file.name"
               display-name-singular="file name"
               display-name-plural="file names"
               description="a name of a computer file"
               data-type="string:0:mc:ur"
               compress="true"
               version="1"/>

computing.file.name.ci
----------------------
*a name of a computer file in a case insensitive file system*

.. code-block:: xml

  <object-type name="computing.file.name.ci"
               display-name-singular="file name"
               display-name-plural="file names"
               description="a name of a computer file in a case insensitive file system"
               data-type="string:0:uc:ur"
               compress="true"
               version="1"/>

computing.file.path
-------------------
*a location on a computer filesystem*

.. code-block:: xml

  <object-type name="computing.file.path"
               display-name-singular="path"
               display-name-plural="paths"
               description="a location on a computer filesystem"
               data-type="string:0:mc:ur"
               compress="true"
               version="1"/>

computing.file.path.ci
----------------------
*a location on a case insensitive computer filesystem*

.. code-block:: xml

  <object-type name="computing.file.path.ci"
               display-name-singular="path"
               display-name-plural="paths"
               description="a location on a case insensitive computer filesystem"
               data-type="string:0:uc:ur"
               compress="true"
               version="1"/>

Concepts
========

entity.physical-entity.object.whole.artifact.instrumentality.device.machine.computer
------------------------------------------------------------------------------------
*a kind of a computing device*

.. code-block:: xml

  <concept name="entity.physical-entity.object.whole.artifact.instrumentality.device.machine.computer"
           display-name-singular="computer"
           display-name-plural="computers"
           description="a kind of a computing device"
           version="1"/>

entity.physical-entity.object.whole.living-thing.organism.person.user
---------------------------------------------------------------------
*a name of a user account on a computer system*

.. code-block:: xml

  <concept name="entity.physical-entity.object.whole.living-thing.organism.person.user"
           display-name-singular="user"
           display-name-plural="users"
           description="a name of a user account on a computer system"
           version="1"/>

entity.abstraction.communication.indication.evidence.record.file
----------------------------------------------------------------
*a computer resource for recording data*

.. code-block:: xml

  <concept name="entity.abstraction.communication.indication.evidence.record.file"
           display-name-singular="file"
           display-name-plural="files"
           description="a computer resource for recording data"
           version="1"/>

