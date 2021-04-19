********
Contents
********

An overview of the ontology elements is provided below.

ForensicsBrick
==============
Object types:

- computing.forensics.filesystem.update-operation_
- computing.forensics.filesystem.entry.type_

WindowsBrick
============
Object types:

- computing.forensics.windows.volume.serial_
- computing.forensics.windows.device.path_
- computing.forensics.windows.drive-letter_
- computing.forensics.windows.sid_
- computing.forensics.windows.eventlog.id_
- computing.forensics.windows.eventlog.severity_
- computing.forensics.windows.eventlog.source_
- computing.forensics.windows.domain_



***********
Definitions
***********

Object Types
============

computing.forensics.filesystem.update-operation
-----------------------------------------------
*a type of operation to update a filesystem entry*

.. code-block:: xml

  <object-type name="computing.forensics.filesystem.update-operation"
               display-name-singular="update operation"
               display-name-plural="update operations"
               description="a type of operation to update a filesystem entry"
               data-type="enum:changed (metadata):modified (content):accessed"
               version="1"/>

computing.forensics.filesystem.entry.type
-----------------------------------------
*a type of filesystem entry*

.. code-block:: xml

  <object-type name="computing.forensics.filesystem.entry.type"
               display-name-singular="filesystem entry type"
               display-name-plural="filesystem entry types"
               description="a type of filesystem entry"
               data-type="enum:file:directory"
               version="1"/>

computing.forensics.windows.volume.serial
-----------------------------------------
*a Windows volume serial number*

.. code-block:: xml

  <object-type name="computing.forensics.windows.volume.serial"
               display-name-singular="volume serial"
               display-name-plural="volume serials"
               description="a Windows volume serial number"
               data-type="hex:4:2:-"
               version="1"/>

computing.forensics.windows.device.path
---------------------------------------
*a Windows device path*

.. code-block:: xml

  <object-type name="computing.forensics.windows.device.path"
               display-name-singular="device path"
               display-name-plural="device paths"
               description="a Windows device path"
               data-type="string:0:mc:u"
               version="1"/>

computing.forensics.windows.drive-letter
----------------------------------------
*a Windows drive letter*

.. code-block:: xml

  <object-type name="computing.forensics.windows.drive-letter"
               display-name-singular="drive letter"
               display-name-plural="drive letters"
               description="a Windows drive letter"
               data-type="string:1:uc"
               version="1"/>

computing.forensics.windows.sid
-------------------------------
*a Windows security identifier*

.. code-block:: xml

  <object-type name="computing.forensics.windows.sid"
               display-name-singular="SID"
               display-name-plural="SIDs"
               description="a Windows security identifier"
               data-type="string:255:mc"
               version="1"/>

computing.forensics.windows.eventlog.id
---------------------------------------
*a message type identifier in a Windows event log*

.. code-block:: xml

  <object-type name="computing.forensics.windows.eventlog.id"
               display-name-singular="Windows event ID"
               display-name-plural="Windows event IDs"
               description="a message type identifier in a Windows event log"
               data-type="number:int"
               version="1"/>

computing.forensics.windows.eventlog.severity
---------------------------------------------
*a message type identifier in a Windows event log*

.. code-block:: xml

  <object-type name="computing.forensics.windows.eventlog.severity"
               display-name-singular="Windows event severity"
               display-name-plural="Windows event severities"
               description="a message type identifier in a Windows event log"
               data-type="number:tinyint"
               version="1"/>

computing.forensics.windows.eventlog.source
-------------------------------------------
*a source of Windows event log messages*

.. code-block:: xml

  <object-type name="computing.forensics.windows.eventlog.source"
               display-name-singular="Windows event source"
               display-name-plural="Windows event sources"
               description="a source of Windows event log messages"
               data-type="string:0:mc:u"
               version="1"/>

computing.forensics.windows.domain
----------------------------------
*a name of a Windows network domain*

.. code-block:: xml

  <object-type name="computing.forensics.windows.domain"
               display-name-singular="windows domain"
               display-name-plural="windows domains"
               description="a name of a Windows network domain"
               data-type="string:0:uc"
               compress="true"
               version="1"/>

