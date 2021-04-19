********
Contents
********

An overview of the ontology elements is provided below.

GeoBrick
========
Object types:

- geo.location.country.iso3166-1-alpha2_
- geo.location.country.name_
- geo.location.region.name_
- geo.location.city.name_
- geo.location.wgs84_



***********
Definitions
***********

Object Types
============

geo.location.country.iso3166-1-alpha2
-------------------------------------
*an ISO 3166-1 alpha-2 country code*

.. code-block:: xml

  <object-type name="geo.location.country.iso3166-1-alpha2"
               display-name-singular="country code"
               display-name-plural="country codes"
               description="an ISO 3166-1 alpha-2 country code"
               data-type="string:2:uc"
               regex-hard="[A-Z]{2}"
               version="1"/>

geo.location.country.name
-------------------------
*a name of a country*

.. code-block:: xml

  <object-type name="geo.location.country.name"
               display-name-singular="country"
               display-name-plural="countries"
               description="a name of a country"
               data-type="string:0:mc:u"
               fuzzy-matching="phonetic"
               version="1"/>

geo.location.region.name
------------------------
*a name of a geopolitical region*

.. code-block:: xml

  <object-type name="geo.location.region.name"
               display-name-singular="region"
               display-name-plural="regions"
               description="a name of a geopolitical region"
               data-type="string:0:mc:u"
               fuzzy-matching="phonetic"
               version="1"/>

geo.location.city.name
----------------------
*a name of a city*

.. code-block:: xml

  <object-type name="geo.location.city.name"
               display-name-singular="city"
               display-name-plural="cities"
               description="a name of a city"
               data-type="string:0:mc:u"
               fuzzy-matching="phonetic"
               version="1"/>

geo.location.wgs84
------------------
*a location on Earth, in the WGS84 coordinate system*

.. code-block:: xml

  <object-type name="geo.location.wgs84"
               display-name-singular="coordinate"
               display-name-plural="coordinates"
               description="a location on Earth, in the WGS84 coordinate system"
               data-type="geo:point"
               version="1"/>

