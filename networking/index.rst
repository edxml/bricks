********
Contents
********

An overview of the ontology elements is provided below.

NetworkingBrick
===============
Object types:

- computing.networking.host.ipv4_
- computing.networking.host.ipv6_
- computing.networking.host.port_
- computing.networking.host.dns-name_
- computing.networking.host.dns-name.wildcard_
- computing.networking.host.mac_
- computing.networking.network.cidr.ipv4_
- computing.networking.network.cidr.ipv6_
- computing.networking.protocol.number_
- computing.networking.protocol.keyword_

Concepts:

- entity.physical-entity.object.whole.artifact.instrumentality.device.machine.computer.router_

HttpBrick
=========
Object types:

- computing.networking.http.resource_
- computing.networking.http.response.status_
- computing.networking.http.method_
- computing.networking.http.query_
- computing.networking.http.user-agent_



***********
Definitions
***********

Object Types
============

computing.networking.host.ipv4
------------------------------
*an IPv4 address of a computer in a computer network*

.. code-block:: xml

  <object-type name="computing.networking.host.ipv4"
               display-name-singular="IPv4 address"
               display-name-plural="IPv4 addresses"
               description="an IPv4 address of a computer in a computer network"
               data-type="ip:v4"
               version="1"/>

computing.networking.host.ipv6
------------------------------
*an IPv6 address of a computer in a computer network*

.. code-block:: xml

  <object-type name="computing.networking.host.ipv6"
               display-name-singular="IPv6 address"
               display-name-plural="IPv6 addresses"
               description="an IPv6 address of a computer in a computer network"
               data-type="ip:v6"
               version="1"/>

computing.networking.host.port
------------------------------
*a TCP/IP networking port, consisting of a number followed by a slash and protocol (TCP or UDP)*

.. code-block:: xml

  <object-type name="computing.networking.host.port"
               display-name-singular="TCP/IP network port"
               display-name-plural="TCP/IP network ports"
               description="a TCP/IP networking port, consisting of a number followed by a slash and protocol (TCP or UDP)"
               data-type="string:64:uc"
               regex-hard="\d+/(TCP|UDP)"
               version="1"/>

computing.networking.host.dns-name
----------------------------------
*a DNS name of a computer in a computer network*

.. code-block:: xml

  <object-type name="computing.networking.host.dns-name"
               display-name-singular="DNS name"
               display-name-plural="DNS names"
               description="a DNS name of a computer in a computer network"
               data-type="string:255:lc:r"
               compress="true"
               fuzzy-matching="[:10]"
               version="1"/>

computing.networking.host.dns-name.wildcard
-------------------------------------------
*a wildcard DNS name of set of computers in a computer network*

.. code-block:: xml

  <object-type name="computing.networking.host.dns-name.wildcard"
               display-name-singular="wildcard host name"
               display-name-plural="wildcard host names"
               description="a wildcard DNS name of set of computers in a computer network"
               data-type="string:255:lc:r"
               compress="true"
               fuzzy-matching="[:10]"
               version="1"/>

computing.networking.host.mac
-----------------------------
*a MAC address of a physical network interface card*

.. code-block:: xml

  <object-type name="computing.networking.host.mac"
               display-name-singular="MAC address"
               display-name-plural="MAC addresses"
               description="a MAC address of a physical network interface card"
               data-type="hex:6:1::"
               version="1"/>

computing.networking.network.cidr.ipv4
--------------------------------------
*a block of IPv4 addresses in CIDR notation*

.. code-block:: xml

  <object-type name="computing.networking.network.cidr.ipv4"
               display-name-singular="IPv4 CIDR"
               display-name-plural="IPv4 CIDRs"
               description="a block of IPv4 addresses in CIDR notation"
               data-type="string:18:mc:u"
               regex-hard="((1?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]).){3}(1?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])/[0-9]{1,2}"
               version="1"/>

computing.networking.network.cidr.ipv6
--------------------------------------
*a block of IPv6 addresses in CIDR notation*

.. code-block:: xml

  <object-type name="computing.networking.network.cidr.ipv6"
               display-name-singular="IPv6 CIDR"
               display-name-plural="IPv6 CIDRs"
               description="a block of IPv6 addresses in CIDR notation"
               data-type="string:43:mc:u"
               regex-hard="[a-f\d]{4}(:[a-f\d]{4}){7}/[\d]{1,3}"
               version="1"/>

computing.networking.protocol.number
------------------------------------
*an IANA internet protocol number*

.. code-block:: xml

  <object-type name="computing.networking.protocol.number"
               display-name-singular="protocol number"
               display-name-plural="protocol numbers"
               description="an IANA internet protocol number"
               data-type="number:tinyint"
               xref="https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml"
               version="1"/>

computing.networking.protocol.keyword
-------------------------------------
*a keyword of an IANA assigned internet protocol*

.. code-block:: xml

  <object-type name="computing.networking.protocol.keyword"
               display-name-singular="internet protocol"
               display-name-plural="internet protocols"
               description="a keyword of an IANA assigned internet protocol"
               data-type="string:24:mc:u"
               xref="https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml"
               version="1"/>

computing.networking.http.resource
----------------------------------
*a locator for an HTTP resource*

.. code-block:: xml

  <object-type name="computing.networking.http.resource"
               display-name-singular="HTTP resource locator"
               display-name-plural="HTTP resource locators"
               description="a locator for an HTTP resource"
               data-type="uri:/"
               compress="true"
               version="1"/>

computing.networking.http.response.status
-----------------------------------------
*an HTTP response status*

.. code-block:: xml

  <object-type name="computing.networking.http.response.status"
               display-name-singular="HTTP response status"
               display-name-plural="HTTP response statuses"
               description="an HTTP response status"
               data-type="number:smallint"
               version="1"/>

computing.networking.http.method
--------------------------------
*an HTTP request method*

.. code-block:: xml

  <object-type name="computing.networking.http.method"
               display-name-singular="HTTP request method"
               display-name-plural="HTTP request methods"
               description="an HTTP request method"
               data-type="string:255:uc"
               version="1"/>

computing.networking.http.query
-------------------------------
*a query part of a HTTP request*

.. code-block:: xml

  <object-type name="computing.networking.http.query"
               display-name-singular="HTTP query"
               display-name-plural="HTTP queries"
               description="a query part of a HTTP request"
               data-type="string:0:mc:u"
               compress="true"
               version="1"/>

computing.networking.http.user-agent
------------------------------------
*an HTTP user agent*

.. code-block:: xml

  <object-type name="computing.networking.http.user-agent"
               display-name-singular="HTTP user agent"
               display-name-plural="HTTP user agents"
               description="an HTTP user agent"
               data-type="string:0:mc:ur"
               compress="true"
               version="1"/>

Concepts
========

entity.physical-entity.object.whole.artifact.instrumentality.device.machine.computer.router
-------------------------------------------------------------------------------------------
*a networking device that forwards data packets between computer networks*

.. code-block:: xml

  <concept name="entity.physical-entity.object.whole.artifact.instrumentality.device.machine.computer.router"
           display-name-singular="network router"
           display-name-plural="network routers"
           description="a networking device that forwards data packets between computer networks"
           version="1"/>

