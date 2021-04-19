********
Contents
********

An overview of the ontology elements is provided below.

SecurityBrick
=============
Object types:

- computing.security.malware.sample.name_
- computing.security.cvss.vector_
- computing.security.cvss.score_
- computing.security.vulnerability.cve_
- computing.security.vulnerability.bid_

Concepts:

- entity.abstraction.communication.written-communication.writing.coding-system.code.software.malware_
- entity.physical-entity.causal-agent.danger.threat_
- entity.abstraction.attribute.state.condition.danger.vulnerability_
- entity.physical-entity.object.whole.artifact.instrumentality.device.machine.computer.vulnerability-scanner_

CryptoBrick
===========
Object types:

- computing.crypto.hash.md5_
- computing.crypto.hash.sha1_
- computing.crypto.hash.sha256_
- computing.crypto.certificate.dn_
- computing.crypto.certificate.cn_
- computing.crypto.certificate.fingerprint.sha1_

Concepts:

- document.deed.certificate.pk-certificate_



***********
Definitions
***********

Object Types
============

computing.security.malware.sample.name
--------------------------------------
*a name of a malware sample*

.. code-block:: xml

  <object-type name="computing.security.malware.sample.name"
               display-name-singular="malware sample name"
               display-name-plural="malware sample names"
               description="a name of a malware sample"
               data-type="string:0:mc:u"
               compress="true"
               version="1"/>

computing.security.cvss.vector
------------------------------
*a base vector in the Common Vulnerability Scoring System*

.. code-block:: xml

  <object-type name="computing.security.cvss.vector"
               display-name-singular="CVSS base vector"
               display-name-plural="CVSS base vectors"
               description="a base vector in the Common Vulnerability Scoring System"
               data-type="string:255:mc"
               compress="true"
               regex-soft="AV:[LAN]/AC:[HML]/Au:[MSN]/C:[NPC]/I:[NPC]/A:[NPC]"
               version="1"/>

computing.security.cvss.score
-----------------------------
*a base score in the Common Vulnerability Scoring System*

.. code-block:: xml

  <object-type name="computing.security.cvss.score"
               display-name-singular="CVSS base score"
               display-name-plural="CVSS base scores"
               description="a base score in the Common Vulnerability Scoring System"
               data-type="number:decimal:3:1"
               version="1"/>

computing.security.vulnerability.cve
------------------------------------
*a unique identifier of a security vulnerability in the CVE dictionary*

.. code-block:: xml

  <object-type name="computing.security.vulnerability.cve"
               display-name-singular="CVE number"
               display-name-plural="CVE numbers"
               description="a unique identifier of a security vulnerability in the CVE dictionary"
               data-type="string:255:uc"
               regex-hard="CVE-[\d]{4}-\d+"
               regex-soft="CVE-202\d-00\d{2}"
               version="1"/>

computing.security.vulnerability.bid
------------------------------------
*a unique identifier of a security vulnerability on Bugtraq*

.. code-block:: xml

  <object-type name="computing.security.vulnerability.bid"
               display-name-singular="BID number"
               display-name-plural="BID numbers"
               description="a unique identifier of a security vulnerability on Bugtraq"
               data-type="number:int"
               version="1"/>

computing.crypto.hash.md5
-------------------------
*an MD5 cryptographic hash*

.. code-block:: xml

  <object-type name="computing.crypto.hash.md5"
               display-name-singular="MD5 hash"
               display-name-plural="MD5 hashes"
               description="an MD5 cryptographic hash"
               data-type="hex:16"
               version="1"/>

computing.crypto.hash.sha1
--------------------------
*a SHA-1 cryptographic hash*

.. code-block:: xml

  <object-type name="computing.crypto.hash.sha1"
               display-name-singular="SHA1 hash"
               display-name-plural="SHA1 hashes"
               description="a SHA-1 cryptographic hash"
               data-type="hex:20"
               version="1"/>

computing.crypto.hash.sha256
----------------------------
*a SHA-256 cryptographic hash*

.. code-block:: xml

  <object-type name="computing.crypto.hash.sha256"
               display-name-singular="SHA256 hash"
               display-name-plural="SHA256 hashes"
               description="a SHA-256 cryptographic hash"
               data-type="hex:32"
               version="1"/>

computing.crypto.certificate.dn
-------------------------------
*a Distinguished Name of a public key certificate*

.. code-block:: xml

  <object-type name="computing.crypto.certificate.dn"
               display-name-singular="Distinguished Name"
               display-name-plural="Distinguished Names"
               description="a Distinguished Name of a public key certificate"
               data-type="string:0:mc:u"
               compress="true"
               version="1"/>

computing.crypto.certificate.cn
-------------------------------
*a Common Name of a public key certificate*

.. code-block:: xml

  <object-type name="computing.crypto.certificate.cn"
               display-name-singular="Common Name"
               display-name-plural="Common Names"
               description="a Common Name of a public key certificate"
               data-type="string:0:mc:u"
               compress="true"
               version="1"/>

computing.crypto.certificate.fingerprint.sha1
---------------------------------------------
*a SHA-1 fingerprint of a public key certificate*

.. code-block:: xml

  <object-type name="computing.crypto.certificate.fingerprint.sha1"
               display-name-singular="certificate fingerprint"
               display-name-plural="certificate fingerprints"
               description="a SHA-1 fingerprint of a public key certificate"
               data-type="hex:20"
               version="1"/>

Concepts
========

entity.abstraction.communication.written-communication.writing.coding-system.code.software.malware
--------------------------------------------------------------------------------------------------
*a malicious computer file*

.. code-block:: xml

  <concept name="entity.abstraction.communication.written-communication.writing.coding-system.code.software.malware"
           display-name-singular="malware sample"
           display-name-plural="malware samples"
           description="a malicious computer file"
           version="1"/>

entity.physical-entity.causal-agent.danger.threat
-------------------------------------------------
*a security threat*

.. code-block:: xml

  <concept name="entity.physical-entity.causal-agent.danger.threat"
           display-name-singular="security threat"
           display-name-plural="security threats"
           description="a security threat"
           version="1"/>

entity.abstraction.attribute.state.condition.danger.vulnerability
-----------------------------------------------------------------
*a security defect reducing a systems's information assurance*

.. code-block:: xml

  <concept name="entity.abstraction.attribute.state.condition.danger.vulnerability"
           display-name-singular="vulnerability"
           display-name-plural="vulnerabilities"
           description="a security defect reducing a systems's information assurance"
           version="1"/>

entity.physical-entity.object.whole.artifact.instrumentality.device.machine.computer.vulnerability-scanner
----------------------------------------------------------------------------------------------------------
*a computer instrumented to perform vulnerability scans*

.. code-block:: xml

  <concept name="entity.physical-entity.object.whole.artifact.instrumentality.device.machine.computer.vulnerability-scanner"
           display-name-singular="vulnerability scanner"
           display-name-plural="vulnerability scanners"
           description="a computer instrumented to perform vulnerability scans"
           version="1"/>

document.deed.certificate.pk-certificate
----------------------------------------
*a cryptographic public key certificate*

.. code-block:: xml

  <concept name="document.deed.certificate.pk-certificate"
           display-name-singular="certificate"
           display-name-plural="certificates"
           description="a cryptographic public key certificate"
           version="1"/>

