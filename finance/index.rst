********
Contents
********

An overview of the ontology elements is provided below.

FinanceBrick
============
Object types:

- finance.banking.bin_
- finance.banking.swift_

Concepts:

- entity.abstraction.group.social-group.organization.company_
- entity.abstraction.group.social-group.organization.company.bank_

CommonCurrenciesBrick
=====================
Object types:

- finance.currency.chf_
- finance.currency.cny_
- finance.currency.eur_
- finance.currency.gbp_
- finance.currency.cad_
- finance.currency.jpy_
- finance.currency.usd_

AllCurrenciesBrick
==================
Object types:

- finance.currency.aed_
- finance.currency.afn_
- finance.currency.all_
- finance.currency.amd_
- finance.currency.ang_
- finance.currency.aoa_
- finance.currency.ars_
- finance.currency.aud_
- finance.currency.awg_
- finance.currency.azn_
- finance.currency.bam_
- finance.currency.bbd_
- finance.currency.bdt_
- finance.currency.bgn_
- finance.currency.bhd_
- finance.currency.bif_
- finance.currency.bmd_
- finance.currency.bnd_
- finance.currency.bob_
- finance.currency.bov_
- finance.currency.brl_
- finance.currency.bsd_
- finance.currency.btn_
- finance.currency.bwp_
- finance.currency.byn_
- finance.currency.bzd_
- finance.currency.cad_
- finance.currency.cdf_
- finance.currency.che_
- finance.currency.chf_
- finance.currency.chw_
- finance.currency.clf_
- finance.currency.clp_
- finance.currency.cny_
- finance.currency.cop_
- finance.currency.cou_
- finance.currency.crc_
- finance.currency.cuc_
- finance.currency.cup_
- finance.currency.cve_
- finance.currency.czk_
- finance.currency.djf_
- finance.currency.dkk_
- finance.currency.dop_
- finance.currency.dzd_
- finance.currency.egp_
- finance.currency.ern_
- finance.currency.etb_
- finance.currency.eur_
- finance.currency.fjd_
- finance.currency.fkp_
- finance.currency.gbp_
- finance.currency.gel_
- finance.currency.ghs_
- finance.currency.gip_
- finance.currency.gmd_
- finance.currency.gnf_
- finance.currency.gtq_
- finance.currency.gyd_
- finance.currency.hkd_
- finance.currency.hnl_
- finance.currency.hrk_
- finance.currency.htg_
- finance.currency.huf_
- finance.currency.idr_
- finance.currency.ils_
- finance.currency.inr_
- finance.currency.iqd_
- finance.currency.irr_
- finance.currency.isk_
- finance.currency.jmd_
- finance.currency.jod_
- finance.currency.jpy_
- finance.currency.kes_
- finance.currency.kgs_
- finance.currency.khr_
- finance.currency.kmf_
- finance.currency.kpw_
- finance.currency.krw_
- finance.currency.kwd_
- finance.currency.kyd_
- finance.currency.kzt_
- finance.currency.lak_
- finance.currency.lbp_
- finance.currency.lkr_
- finance.currency.lrd_
- finance.currency.lsl_
- finance.currency.lyd_
- finance.currency.mad_
- finance.currency.mdl_
- finance.currency.mga_
- finance.currency.mkd_
- finance.currency.mmk_
- finance.currency.mnt_
- finance.currency.mop_
- finance.currency.mru_
- finance.currency.mur_
- finance.currency.mvr_
- finance.currency.mwk_
- finance.currency.mxn_
- finance.currency.myr_
- finance.currency.mzn_
- finance.currency.nad_
- finance.currency.ngn_
- finance.currency.nio_
- finance.currency.nok_
- finance.currency.npr_
- finance.currency.nzd_
- finance.currency.omr_
- finance.currency.pab_
- finance.currency.pen_
- finance.currency.pgk_
- finance.currency.php_
- finance.currency.pkr_
- finance.currency.pln_
- finance.currency.pyg_
- finance.currency.qar_
- finance.currency.ron_
- finance.currency.rsd_
- finance.currency.rub_
- finance.currency.rwf_
- finance.currency.sar_
- finance.currency.sbd_
- finance.currency.scr_
- finance.currency.sdg_
- finance.currency.sek_
- finance.currency.sgd_
- finance.currency.shp_
- finance.currency.sll_
- finance.currency.sos_
- finance.currency.srd_
- finance.currency.ssp_
- finance.currency.stn_
- finance.currency.svc_
- finance.currency.syp_
- finance.currency.szl_
- finance.currency.thb_
- finance.currency.tjs_
- finance.currency.tmt_
- finance.currency.tnd_
- finance.currency.top_
- finance.currency.try_
- finance.currency.ttd_
- finance.currency.twd_
- finance.currency.tzs_
- finance.currency.uah_
- finance.currency.ugx_
- finance.currency.usd_
- finance.currency.uyu_
- finance.currency.uyw_
- finance.currency.uzs_
- finance.currency.ves_
- finance.currency.vnd_
- finance.currency.vuv_
- finance.currency.wst_
- finance.currency.xaf_
- finance.currency.xcd_
- finance.currency.xof_
- finance.currency.xpf_
- finance.currency.xsu_
- finance.currency.xua_
- finance.currency.yer_
- finance.currency.zar_
- finance.currency.zmw_
- finance.currency.zwl_



***********
Definitions
***********

Object Types
============

finance.banking.bin
-------------------
*a Bank Identification Number of a payment card*

.. code-block:: xml

  <object-type name="finance.banking.bin"
               display-name-singular="BIN"
               display-name-plural="BINs"
               description="a Bank Identification Number of a payment card"
               data-type="string:16:mc:u"
               xref="https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)"
               regex-hard="[\d]+"
               version="1"/>

finance.banking.swift
---------------------
*an ISO 9362 Business Identifier Code (BIC)*

.. code-block:: xml

  <object-type name="finance.banking.swift"
               display-name-singular="SWIFT code"
               display-name-plural="SWIFT codes"
               description="an ISO 9362 Business Identifier Code (BIC)"
               data-type="string:11:mc:u"
               xref="https://en.wikipedia.org/wiki/ISO_9362"
               regex-hard="[\dA-Z]+"
               regex-soft="[A-Z]{8}([A-Z]{3})?"
               version="1"/>

finance.currency.chf
--------------------
*an amount of Swiss Francs*

.. code-block:: xml

  <object-type name="finance.currency.chf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Swiss Francs"
               data-type="number:currency"
               unit-name="Swiss Franc"
               unit-symbol="CHF"
               version="1"/>

finance.currency.cny
--------------------
*an amount of Yuan Renminbis*

.. code-block:: xml

  <object-type name="finance.currency.cny"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Yuan Renminbis"
               data-type="number:currency"
               unit-name="Yuan Renminbi"
               unit-symbol="CNY"
               version="1"/>

finance.currency.eur
--------------------
*an amount of Euros*

.. code-block:: xml

  <object-type name="finance.currency.eur"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Euros"
               data-type="number:currency"
               unit-name="Euro"
               unit-symbol="EUR"
               version="1"/>

finance.currency.gbp
--------------------
*an amount of Pound Sterlings*

.. code-block:: xml

  <object-type name="finance.currency.gbp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Pound Sterlings"
               data-type="number:currency"
               unit-name="Pound Sterling"
               unit-symbol="GBP"
               version="1"/>

finance.currency.cad
--------------------
*an amount of Canadian Dollars*

.. code-block:: xml

  <object-type name="finance.currency.cad"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Canadian Dollars"
               data-type="number:currency"
               unit-name="Canadian Dollar"
               unit-symbol="CAD"
               version="1"/>

finance.currency.jpy
--------------------
*an amount of Yens*

.. code-block:: xml

  <object-type name="finance.currency.jpy"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Yens"
               data-type="number:currency"
               unit-name="Yen"
               unit-symbol="JPY"
               version="1"/>

finance.currency.usd
--------------------
*an amount of US Dollars*

.. code-block:: xml

  <object-type name="finance.currency.usd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of US Dollars"
               data-type="number:currency"
               unit-name="US Dollar"
               unit-symbol="USD"
               version="1"/>

finance.currency.aed
--------------------
*an amount of UAE Dirhams*

.. code-block:: xml

  <object-type name="finance.currency.aed"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of UAE Dirhams"
               data-type="number:currency"
               unit-name="UAE Dirham"
               unit-symbol="AED"
               version="1"/>

finance.currency.afn
--------------------
*an amount of Afghanis*

.. code-block:: xml

  <object-type name="finance.currency.afn"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Afghanis"
               data-type="number:currency"
               unit-name="Afghani"
               unit-symbol="AFN"
               version="1"/>

finance.currency.all
--------------------
*an amount of Leks*

.. code-block:: xml

  <object-type name="finance.currency.all"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Leks"
               data-type="number:currency"
               unit-name="Lek"
               unit-symbol="ALL"
               version="1"/>

finance.currency.amd
--------------------
*an amount of Armenian Drams*

.. code-block:: xml

  <object-type name="finance.currency.amd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Armenian Drams"
               data-type="number:currency"
               unit-name="Armenian Dram"
               unit-symbol="AMD"
               version="1"/>

finance.currency.ang
--------------------
*an amount of Netherlands Antillean Guilders*

.. code-block:: xml

  <object-type name="finance.currency.ang"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Netherlands Antillean Guilders"
               data-type="number:currency"
               unit-name="Netherlands Antillean Guilder"
               unit-symbol="ANG"
               version="1"/>

finance.currency.aoa
--------------------
*an amount of Kwanzas*

.. code-block:: xml

  <object-type name="finance.currency.aoa"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Kwanzas"
               data-type="number:currency"
               unit-name="Kwanza"
               unit-symbol="AOA"
               version="1"/>

finance.currency.ars
--------------------
*an amount of Argentine Pesos*

.. code-block:: xml

  <object-type name="finance.currency.ars"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Argentine Pesos"
               data-type="number:currency"
               unit-name="Argentine Peso"
               unit-symbol="ARS"
               version="1"/>

finance.currency.aud
--------------------
*an amount of Australian Dollars*

.. code-block:: xml

  <object-type name="finance.currency.aud"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Australian Dollars"
               data-type="number:currency"
               unit-name="Australian Dollar"
               unit-symbol="AUD"
               version="1"/>

finance.currency.awg
--------------------
*an amount of Aruban Florins*

.. code-block:: xml

  <object-type name="finance.currency.awg"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Aruban Florins"
               data-type="number:currency"
               unit-name="Aruban Florin"
               unit-symbol="AWG"
               version="1"/>

finance.currency.azn
--------------------
*an amount of Azerbaijan Manats*

.. code-block:: xml

  <object-type name="finance.currency.azn"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Azerbaijan Manats"
               data-type="number:currency"
               unit-name="Azerbaijan Manat"
               unit-symbol="AZN"
               version="1"/>

finance.currency.bam
--------------------
*an amount of Convertible Marks*

.. code-block:: xml

  <object-type name="finance.currency.bam"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Convertible Marks"
               data-type="number:currency"
               unit-name="Convertible Mark"
               unit-symbol="BAM"
               version="1"/>

finance.currency.bbd
--------------------
*an amount of Barbados Dollars*

.. code-block:: xml

  <object-type name="finance.currency.bbd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Barbados Dollars"
               data-type="number:currency"
               unit-name="Barbados Dollar"
               unit-symbol="BBD"
               version="1"/>

finance.currency.bdt
--------------------
*an amount of Takas*

.. code-block:: xml

  <object-type name="finance.currency.bdt"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Takas"
               data-type="number:currency"
               unit-name="Taka"
               unit-symbol="BDT"
               version="1"/>

finance.currency.bgn
--------------------
*an amount of Bulgarian Levs*

.. code-block:: xml

  <object-type name="finance.currency.bgn"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Bulgarian Levs"
               data-type="number:currency"
               unit-name="Bulgarian Lev"
               unit-symbol="BGN"
               version="1"/>

finance.currency.bhd
--------------------
*an amount of Bahraini Dinars*

.. code-block:: xml

  <object-type name="finance.currency.bhd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Bahraini Dinars"
               data-type="number:currency"
               unit-name="Bahraini Dinar"
               unit-symbol="BHD"
               version="1"/>

finance.currency.bif
--------------------
*an amount of Burundi Francs*

.. code-block:: xml

  <object-type name="finance.currency.bif"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Burundi Francs"
               data-type="number:currency"
               unit-name="Burundi Franc"
               unit-symbol="BIF"
               version="1"/>

finance.currency.bmd
--------------------
*an amount of Bermudian Dollars*

.. code-block:: xml

  <object-type name="finance.currency.bmd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Bermudian Dollars"
               data-type="number:currency"
               unit-name="Bermudian Dollar"
               unit-symbol="BMD"
               version="1"/>

finance.currency.bnd
--------------------
*an amount of Brunei Dollars*

.. code-block:: xml

  <object-type name="finance.currency.bnd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Brunei Dollars"
               data-type="number:currency"
               unit-name="Brunei Dollar"
               unit-symbol="BND"
               version="1"/>

finance.currency.bob
--------------------
*an amount of Bolivianos*

.. code-block:: xml

  <object-type name="finance.currency.bob"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Bolivianos"
               data-type="number:currency"
               unit-name="Boliviano"
               unit-symbol="BOB"
               version="1"/>

finance.currency.bov
--------------------
*an amount of Mvdols*

.. code-block:: xml

  <object-type name="finance.currency.bov"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Mvdols"
               data-type="number:currency"
               unit-name="Mvdol"
               unit-symbol="BOV"
               version="1"/>

finance.currency.brl
--------------------
*an amount of Brazilian Reals*

.. code-block:: xml

  <object-type name="finance.currency.brl"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Brazilian Reals"
               data-type="number:currency"
               unit-name="Brazilian Real"
               unit-symbol="BRL"
               version="1"/>

finance.currency.bsd
--------------------
*an amount of Bahamian Dollars*

.. code-block:: xml

  <object-type name="finance.currency.bsd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Bahamian Dollars"
               data-type="number:currency"
               unit-name="Bahamian Dollar"
               unit-symbol="BSD"
               version="1"/>

finance.currency.btn
--------------------
*an amount of Ngultrums*

.. code-block:: xml

  <object-type name="finance.currency.btn"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Ngultrums"
               data-type="number:currency"
               unit-name="Ngultrum"
               unit-symbol="BTN"
               version="1"/>

finance.currency.bwp
--------------------
*an amount of Pulas*

.. code-block:: xml

  <object-type name="finance.currency.bwp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Pulas"
               data-type="number:currency"
               unit-name="Pula"
               unit-symbol="BWP"
               version="1"/>

finance.currency.byn
--------------------
*an amount of Belarusian Rubles*

.. code-block:: xml

  <object-type name="finance.currency.byn"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Belarusian Rubles"
               data-type="number:currency"
               unit-name="Belarusian Ruble"
               unit-symbol="BYN"
               version="1"/>

finance.currency.bzd
--------------------
*an amount of Belize Dollars*

.. code-block:: xml

  <object-type name="finance.currency.bzd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Belize Dollars"
               data-type="number:currency"
               unit-name="Belize Dollar"
               unit-symbol="BZD"
               version="1"/>

finance.currency.cad
--------------------
*an amount of Canadian Dollars*

.. code-block:: xml

  <object-type name="finance.currency.cad"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Canadian Dollars"
               data-type="number:currency"
               unit-name="Canadian Dollar"
               unit-symbol="CAD"
               version="1"/>

finance.currency.cdf
--------------------
*an amount of Congolese Francs*

.. code-block:: xml

  <object-type name="finance.currency.cdf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Congolese Francs"
               data-type="number:currency"
               unit-name="Congolese Franc"
               unit-symbol="CDF"
               version="1"/>

finance.currency.che
--------------------
*an amount of WIR Euros*

.. code-block:: xml

  <object-type name="finance.currency.che"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of WIR Euros"
               data-type="number:currency"
               unit-name="WIR Euro"
               unit-symbol="CHE"
               version="1"/>

finance.currency.chf
--------------------
*an amount of Swiss Francs*

.. code-block:: xml

  <object-type name="finance.currency.chf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Swiss Francs"
               data-type="number:currency"
               unit-name="Swiss Franc"
               unit-symbol="CHF"
               version="1"/>

finance.currency.chw
--------------------
*an amount of WIR Francs*

.. code-block:: xml

  <object-type name="finance.currency.chw"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of WIR Francs"
               data-type="number:currency"
               unit-name="WIR Franc"
               unit-symbol="CHW"
               version="1"/>

finance.currency.clf
--------------------
*an amount of Unidad de Fomentos*

.. code-block:: xml

  <object-type name="finance.currency.clf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Unidad de Fomentos"
               data-type="number:currency"
               unit-name="Unidad de Fomento"
               unit-symbol="CLF"
               version="1"/>

finance.currency.clp
--------------------
*an amount of Chilean Pesos*

.. code-block:: xml

  <object-type name="finance.currency.clp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Chilean Pesos"
               data-type="number:currency"
               unit-name="Chilean Peso"
               unit-symbol="CLP"
               version="1"/>

finance.currency.cny
--------------------
*an amount of Yuan Renminbis*

.. code-block:: xml

  <object-type name="finance.currency.cny"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Yuan Renminbis"
               data-type="number:currency"
               unit-name="Yuan Renminbi"
               unit-symbol="CNY"
               version="1"/>

finance.currency.cop
--------------------
*an amount of Colombian Pesos*

.. code-block:: xml

  <object-type name="finance.currency.cop"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Colombian Pesos"
               data-type="number:currency"
               unit-name="Colombian Peso"
               unit-symbol="COP"
               version="1"/>

finance.currency.cou
--------------------
*an amount of Unidad de Valor Reals*

.. code-block:: xml

  <object-type name="finance.currency.cou"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Unidad de Valor Reals"
               data-type="number:currency"
               unit-name="Unidad de Valor Real"
               unit-symbol="COU"
               version="1"/>

finance.currency.crc
--------------------
*an amount of Costa Rican Colons*

.. code-block:: xml

  <object-type name="finance.currency.crc"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Costa Rican Colons"
               data-type="number:currency"
               unit-name="Costa Rican Colon"
               unit-symbol="CRC"
               version="1"/>

finance.currency.cuc
--------------------
*an amount of Peso Convertibles*

.. code-block:: xml

  <object-type name="finance.currency.cuc"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Peso Convertibles"
               data-type="number:currency"
               unit-name="Peso Convertible"
               unit-symbol="CUC"
               version="1"/>

finance.currency.cup
--------------------
*an amount of Cuban Pesos*

.. code-block:: xml

  <object-type name="finance.currency.cup"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Cuban Pesos"
               data-type="number:currency"
               unit-name="Cuban Peso"
               unit-symbol="CUP"
               version="1"/>

finance.currency.cve
--------------------
*an amount of Cabo Verde Escudos*

.. code-block:: xml

  <object-type name="finance.currency.cve"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Cabo Verde Escudos"
               data-type="number:currency"
               unit-name="Cabo Verde Escudo"
               unit-symbol="CVE"
               version="1"/>

finance.currency.czk
--------------------
*an amount of Czech Korunas*

.. code-block:: xml

  <object-type name="finance.currency.czk"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Czech Korunas"
               data-type="number:currency"
               unit-name="Czech Koruna"
               unit-symbol="CZK"
               version="1"/>

finance.currency.djf
--------------------
*an amount of Djibouti Francs*

.. code-block:: xml

  <object-type name="finance.currency.djf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Djibouti Francs"
               data-type="number:currency"
               unit-name="Djibouti Franc"
               unit-symbol="DJF"
               version="1"/>

finance.currency.dkk
--------------------
*an amount of Danish Krones*

.. code-block:: xml

  <object-type name="finance.currency.dkk"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Danish Krones"
               data-type="number:currency"
               unit-name="Danish Krone"
               unit-symbol="DKK"
               version="1"/>

finance.currency.dop
--------------------
*an amount of Dominican Pesos*

.. code-block:: xml

  <object-type name="finance.currency.dop"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Dominican Pesos"
               data-type="number:currency"
               unit-name="Dominican Peso"
               unit-symbol="DOP"
               version="1"/>

finance.currency.dzd
--------------------
*an amount of Algerian Dinars*

.. code-block:: xml

  <object-type name="finance.currency.dzd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Algerian Dinars"
               data-type="number:currency"
               unit-name="Algerian Dinar"
               unit-symbol="DZD"
               version="1"/>

finance.currency.egp
--------------------
*an amount of Egyptian Pounds*

.. code-block:: xml

  <object-type name="finance.currency.egp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Egyptian Pounds"
               data-type="number:currency"
               unit-name="Egyptian Pound"
               unit-symbol="EGP"
               version="1"/>

finance.currency.ern
--------------------
*an amount of Nakfas*

.. code-block:: xml

  <object-type name="finance.currency.ern"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Nakfas"
               data-type="number:currency"
               unit-name="Nakfa"
               unit-symbol="ERN"
               version="1"/>

finance.currency.etb
--------------------
*an amount of Ethiopian Birrs*

.. code-block:: xml

  <object-type name="finance.currency.etb"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Ethiopian Birrs"
               data-type="number:currency"
               unit-name="Ethiopian Birr"
               unit-symbol="ETB"
               version="1"/>

finance.currency.eur
--------------------
*an amount of Euros*

.. code-block:: xml

  <object-type name="finance.currency.eur"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Euros"
               data-type="number:currency"
               unit-name="Euro"
               unit-symbol="EUR"
               version="1"/>

finance.currency.fjd
--------------------
*an amount of Fiji Dollars*

.. code-block:: xml

  <object-type name="finance.currency.fjd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Fiji Dollars"
               data-type="number:currency"
               unit-name="Fiji Dollar"
               unit-symbol="FJD"
               version="1"/>

finance.currency.fkp
--------------------
*an amount of Falkland Islands Pounds*

.. code-block:: xml

  <object-type name="finance.currency.fkp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Falkland Islands Pounds"
               data-type="number:currency"
               unit-name="Falkland Islands Pound"
               unit-symbol="FKP"
               version="1"/>

finance.currency.gbp
--------------------
*an amount of Pound Sterlings*

.. code-block:: xml

  <object-type name="finance.currency.gbp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Pound Sterlings"
               data-type="number:currency"
               unit-name="Pound Sterling"
               unit-symbol="GBP"
               version="1"/>

finance.currency.gel
--------------------
*an amount of Laris*

.. code-block:: xml

  <object-type name="finance.currency.gel"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Laris"
               data-type="number:currency"
               unit-name="Lari"
               unit-symbol="GEL"
               version="1"/>

finance.currency.ghs
--------------------
*an amount of Ghana Cedis*

.. code-block:: xml

  <object-type name="finance.currency.ghs"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Ghana Cedis"
               data-type="number:currency"
               unit-name="Ghana Cedi"
               unit-symbol="GHS"
               version="1"/>

finance.currency.gip
--------------------
*an amount of Gibraltar Pounds*

.. code-block:: xml

  <object-type name="finance.currency.gip"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Gibraltar Pounds"
               data-type="number:currency"
               unit-name="Gibraltar Pound"
               unit-symbol="GIP"
               version="1"/>

finance.currency.gmd
--------------------
*an amount of Dalasis*

.. code-block:: xml

  <object-type name="finance.currency.gmd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Dalasis"
               data-type="number:currency"
               unit-name="Dalasi"
               unit-symbol="GMD"
               version="1"/>

finance.currency.gnf
--------------------
*an amount of Guinean Francs*

.. code-block:: xml

  <object-type name="finance.currency.gnf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Guinean Francs"
               data-type="number:currency"
               unit-name="Guinean Franc"
               unit-symbol="GNF"
               version="1"/>

finance.currency.gtq
--------------------
*an amount of Quetzals*

.. code-block:: xml

  <object-type name="finance.currency.gtq"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Quetzals"
               data-type="number:currency"
               unit-name="Quetzal"
               unit-symbol="GTQ"
               version="1"/>

finance.currency.gyd
--------------------
*an amount of Guyana Dollars*

.. code-block:: xml

  <object-type name="finance.currency.gyd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Guyana Dollars"
               data-type="number:currency"
               unit-name="Guyana Dollar"
               unit-symbol="GYD"
               version="1"/>

finance.currency.hkd
--------------------
*an amount of Hong Kong Dollars*

.. code-block:: xml

  <object-type name="finance.currency.hkd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Hong Kong Dollars"
               data-type="number:currency"
               unit-name="Hong Kong Dollar"
               unit-symbol="HKD"
               version="1"/>

finance.currency.hnl
--------------------
*an amount of Lempiras*

.. code-block:: xml

  <object-type name="finance.currency.hnl"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Lempiras"
               data-type="number:currency"
               unit-name="Lempira"
               unit-symbol="HNL"
               version="1"/>

finance.currency.hrk
--------------------
*an amount of Kunas*

.. code-block:: xml

  <object-type name="finance.currency.hrk"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Kunas"
               data-type="number:currency"
               unit-name="Kuna"
               unit-symbol="HRK"
               version="1"/>

finance.currency.htg
--------------------
*an amount of Gourdes*

.. code-block:: xml

  <object-type name="finance.currency.htg"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Gourdes"
               data-type="number:currency"
               unit-name="Gourde"
               unit-symbol="HTG"
               version="1"/>

finance.currency.huf
--------------------
*an amount of Forints*

.. code-block:: xml

  <object-type name="finance.currency.huf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Forints"
               data-type="number:currency"
               unit-name="Forint"
               unit-symbol="HUF"
               version="1"/>

finance.currency.idr
--------------------
*an amount of Rupiahs*

.. code-block:: xml

  <object-type name="finance.currency.idr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Rupiahs"
               data-type="number:currency"
               unit-name="Rupiah"
               unit-symbol="IDR"
               version="1"/>

finance.currency.ils
--------------------
*an amount of New Israeli Sheqels*

.. code-block:: xml

  <object-type name="finance.currency.ils"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of New Israeli Sheqels"
               data-type="number:currency"
               unit-name="New Israeli Sheqel"
               unit-symbol="ILS"
               version="1"/>

finance.currency.inr
--------------------
*an amount of Indian Rupees*

.. code-block:: xml

  <object-type name="finance.currency.inr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Indian Rupees"
               data-type="number:currency"
               unit-name="Indian Rupee"
               unit-symbol="INR"
               version="1"/>

finance.currency.iqd
--------------------
*an amount of Iraqi Dinars*

.. code-block:: xml

  <object-type name="finance.currency.iqd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Iraqi Dinars"
               data-type="number:currency"
               unit-name="Iraqi Dinar"
               unit-symbol="IQD"
               version="1"/>

finance.currency.irr
--------------------
*an amount of Iranian Rials*

.. code-block:: xml

  <object-type name="finance.currency.irr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Iranian Rials"
               data-type="number:currency"
               unit-name="Iranian Rial"
               unit-symbol="IRR"
               version="1"/>

finance.currency.isk
--------------------
*an amount of Iceland Kronas*

.. code-block:: xml

  <object-type name="finance.currency.isk"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Iceland Kronas"
               data-type="number:currency"
               unit-name="Iceland Krona"
               unit-symbol="ISK"
               version="1"/>

finance.currency.jmd
--------------------
*an amount of Jamaican Dollars*

.. code-block:: xml

  <object-type name="finance.currency.jmd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Jamaican Dollars"
               data-type="number:currency"
               unit-name="Jamaican Dollar"
               unit-symbol="JMD"
               version="1"/>

finance.currency.jod
--------------------
*an amount of Jordanian Dinars*

.. code-block:: xml

  <object-type name="finance.currency.jod"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Jordanian Dinars"
               data-type="number:currency"
               unit-name="Jordanian Dinar"
               unit-symbol="JOD"
               version="1"/>

finance.currency.jpy
--------------------
*an amount of Yens*

.. code-block:: xml

  <object-type name="finance.currency.jpy"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Yens"
               data-type="number:currency"
               unit-name="Yen"
               unit-symbol="JPY"
               version="1"/>

finance.currency.kes
--------------------
*an amount of Kenyan Shillings*

.. code-block:: xml

  <object-type name="finance.currency.kes"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Kenyan Shillings"
               data-type="number:currency"
               unit-name="Kenyan Shilling"
               unit-symbol="KES"
               version="1"/>

finance.currency.kgs
--------------------
*an amount of Soms*

.. code-block:: xml

  <object-type name="finance.currency.kgs"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Soms"
               data-type="number:currency"
               unit-name="Som"
               unit-symbol="KGS"
               version="1"/>

finance.currency.khr
--------------------
*an amount of Riels*

.. code-block:: xml

  <object-type name="finance.currency.khr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Riels"
               data-type="number:currency"
               unit-name="Riel"
               unit-symbol="KHR"
               version="1"/>

finance.currency.kmf
--------------------
*an amount of Comorian Francs*

.. code-block:: xml

  <object-type name="finance.currency.kmf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Comorian Francs"
               data-type="number:currency"
               unit-name="Comorian Franc"
               unit-symbol="KMF"
               version="1"/>

finance.currency.kpw
--------------------
*an amount of North Korean Wons*

.. code-block:: xml

  <object-type name="finance.currency.kpw"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of North Korean Wons"
               data-type="number:currency"
               unit-name="North Korean Won"
               unit-symbol="KPW"
               version="1"/>

finance.currency.krw
--------------------
*an amount of Wons*

.. code-block:: xml

  <object-type name="finance.currency.krw"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Wons"
               data-type="number:currency"
               unit-name="Won"
               unit-symbol="KRW"
               version="1"/>

finance.currency.kwd
--------------------
*an amount of Kuwaiti Dinars*

.. code-block:: xml

  <object-type name="finance.currency.kwd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Kuwaiti Dinars"
               data-type="number:currency"
               unit-name="Kuwaiti Dinar"
               unit-symbol="KWD"
               version="1"/>

finance.currency.kyd
--------------------
*an amount of Cayman Islands Dollars*

.. code-block:: xml

  <object-type name="finance.currency.kyd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Cayman Islands Dollars"
               data-type="number:currency"
               unit-name="Cayman Islands Dollar"
               unit-symbol="KYD"
               version="1"/>

finance.currency.kzt
--------------------
*an amount of Tenges*

.. code-block:: xml

  <object-type name="finance.currency.kzt"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Tenges"
               data-type="number:currency"
               unit-name="Tenge"
               unit-symbol="KZT"
               version="1"/>

finance.currency.lak
--------------------
*an amount of Lao Kips*

.. code-block:: xml

  <object-type name="finance.currency.lak"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Lao Kips"
               data-type="number:currency"
               unit-name="Lao Kip"
               unit-symbol="LAK"
               version="1"/>

finance.currency.lbp
--------------------
*an amount of Lebanese Pounds*

.. code-block:: xml

  <object-type name="finance.currency.lbp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Lebanese Pounds"
               data-type="number:currency"
               unit-name="Lebanese Pound"
               unit-symbol="LBP"
               version="1"/>

finance.currency.lkr
--------------------
*an amount of Sri Lanka Rupees*

.. code-block:: xml

  <object-type name="finance.currency.lkr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Sri Lanka Rupees"
               data-type="number:currency"
               unit-name="Sri Lanka Rupee"
               unit-symbol="LKR"
               version="1"/>

finance.currency.lrd
--------------------
*an amount of Liberian Dollars*

.. code-block:: xml

  <object-type name="finance.currency.lrd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Liberian Dollars"
               data-type="number:currency"
               unit-name="Liberian Dollar"
               unit-symbol="LRD"
               version="1"/>

finance.currency.lsl
--------------------
*an amount of Lotis*

.. code-block:: xml

  <object-type name="finance.currency.lsl"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Lotis"
               data-type="number:currency"
               unit-name="Loti"
               unit-symbol="LSL"
               version="1"/>

finance.currency.lyd
--------------------
*an amount of Libyan Dinars*

.. code-block:: xml

  <object-type name="finance.currency.lyd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Libyan Dinars"
               data-type="number:currency"
               unit-name="Libyan Dinar"
               unit-symbol="LYD"
               version="1"/>

finance.currency.mad
--------------------
*an amount of Moroccan Dirhams*

.. code-block:: xml

  <object-type name="finance.currency.mad"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Moroccan Dirhams"
               data-type="number:currency"
               unit-name="Moroccan Dirham"
               unit-symbol="MAD"
               version="1"/>

finance.currency.mdl
--------------------
*an amount of Moldovan Leus*

.. code-block:: xml

  <object-type name="finance.currency.mdl"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Moldovan Leus"
               data-type="number:currency"
               unit-name="Moldovan Leu"
               unit-symbol="MDL"
               version="1"/>

finance.currency.mga
--------------------
*an amount of Malagasy Ariarys*

.. code-block:: xml

  <object-type name="finance.currency.mga"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Malagasy Ariarys"
               data-type="number:currency"
               unit-name="Malagasy Ariary"
               unit-symbol="MGA"
               version="1"/>

finance.currency.mkd
--------------------
*an amount of Denars*

.. code-block:: xml

  <object-type name="finance.currency.mkd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Denars"
               data-type="number:currency"
               unit-name="Denar"
               unit-symbol="MKD"
               version="1"/>

finance.currency.mmk
--------------------
*an amount of Kyats*

.. code-block:: xml

  <object-type name="finance.currency.mmk"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Kyats"
               data-type="number:currency"
               unit-name="Kyat"
               unit-symbol="MMK"
               version="1"/>

finance.currency.mnt
--------------------
*an amount of Tugriks*

.. code-block:: xml

  <object-type name="finance.currency.mnt"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Tugriks"
               data-type="number:currency"
               unit-name="Tugrik"
               unit-symbol="MNT"
               version="1"/>

finance.currency.mop
--------------------
*an amount of Patacas*

.. code-block:: xml

  <object-type name="finance.currency.mop"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Patacas"
               data-type="number:currency"
               unit-name="Pataca"
               unit-symbol="MOP"
               version="1"/>

finance.currency.mru
--------------------
*an amount of Ouguiyas*

.. code-block:: xml

  <object-type name="finance.currency.mru"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Ouguiyas"
               data-type="number:currency"
               unit-name="Ouguiya"
               unit-symbol="MRU"
               version="1"/>

finance.currency.mur
--------------------
*an amount of Mauritius Rupees*

.. code-block:: xml

  <object-type name="finance.currency.mur"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Mauritius Rupees"
               data-type="number:currency"
               unit-name="Mauritius Rupee"
               unit-symbol="MUR"
               version="1"/>

finance.currency.mvr
--------------------
*an amount of Rufiyaas*

.. code-block:: xml

  <object-type name="finance.currency.mvr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Rufiyaas"
               data-type="number:currency"
               unit-name="Rufiyaa"
               unit-symbol="MVR"
               version="1"/>

finance.currency.mwk
--------------------
*an amount of Malawi Kwachas*

.. code-block:: xml

  <object-type name="finance.currency.mwk"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Malawi Kwachas"
               data-type="number:currency"
               unit-name="Malawi Kwacha"
               unit-symbol="MWK"
               version="1"/>

finance.currency.mxn
--------------------
*an amount of Mexican Pesos*

.. code-block:: xml

  <object-type name="finance.currency.mxn"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Mexican Pesos"
               data-type="number:currency"
               unit-name="Mexican Peso"
               unit-symbol="MXN"
               version="1"/>

finance.currency.myr
--------------------
*an amount of Malaysian Ringgits*

.. code-block:: xml

  <object-type name="finance.currency.myr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Malaysian Ringgits"
               data-type="number:currency"
               unit-name="Malaysian Ringgit"
               unit-symbol="MYR"
               version="1"/>

finance.currency.mzn
--------------------
*an amount of Mozambique Meticals*

.. code-block:: xml

  <object-type name="finance.currency.mzn"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Mozambique Meticals"
               data-type="number:currency"
               unit-name="Mozambique Metical"
               unit-symbol="MZN"
               version="1"/>

finance.currency.nad
--------------------
*an amount of Namibia Dollars*

.. code-block:: xml

  <object-type name="finance.currency.nad"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Namibia Dollars"
               data-type="number:currency"
               unit-name="Namibia Dollar"
               unit-symbol="NAD"
               version="1"/>

finance.currency.ngn
--------------------
*an amount of Nairas*

.. code-block:: xml

  <object-type name="finance.currency.ngn"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Nairas"
               data-type="number:currency"
               unit-name="Naira"
               unit-symbol="NGN"
               version="1"/>

finance.currency.nio
--------------------
*an amount of Cordoba Oros*

.. code-block:: xml

  <object-type name="finance.currency.nio"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Cordoba Oros"
               data-type="number:currency"
               unit-name="Cordoba Oro"
               unit-symbol="NIO"
               version="1"/>

finance.currency.nok
--------------------
*an amount of Norwegian Krones*

.. code-block:: xml

  <object-type name="finance.currency.nok"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Norwegian Krones"
               data-type="number:currency"
               unit-name="Norwegian Krone"
               unit-symbol="NOK"
               version="1"/>

finance.currency.npr
--------------------
*an amount of Nepalese Rupees*

.. code-block:: xml

  <object-type name="finance.currency.npr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Nepalese Rupees"
               data-type="number:currency"
               unit-name="Nepalese Rupee"
               unit-symbol="NPR"
               version="1"/>

finance.currency.nzd
--------------------
*an amount of New Zealand Dollars*

.. code-block:: xml

  <object-type name="finance.currency.nzd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of New Zealand Dollars"
               data-type="number:currency"
               unit-name="New Zealand Dollar"
               unit-symbol="NZD"
               version="1"/>

finance.currency.omr
--------------------
*an amount of Rial Omanis*

.. code-block:: xml

  <object-type name="finance.currency.omr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Rial Omanis"
               data-type="number:currency"
               unit-name="Rial Omani"
               unit-symbol="OMR"
               version="1"/>

finance.currency.pab
--------------------
*an amount of Balboas*

.. code-block:: xml

  <object-type name="finance.currency.pab"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Balboas"
               data-type="number:currency"
               unit-name="Balboa"
               unit-symbol="PAB"
               version="1"/>

finance.currency.pen
--------------------
*an amount of Sols*

.. code-block:: xml

  <object-type name="finance.currency.pen"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Sols"
               data-type="number:currency"
               unit-name="Sol"
               unit-symbol="PEN"
               version="1"/>

finance.currency.pgk
--------------------
*an amount of Kinas*

.. code-block:: xml

  <object-type name="finance.currency.pgk"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Kinas"
               data-type="number:currency"
               unit-name="Kina"
               unit-symbol="PGK"
               version="1"/>

finance.currency.php
--------------------
*an amount of Philippine Pesos*

.. code-block:: xml

  <object-type name="finance.currency.php"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Philippine Pesos"
               data-type="number:currency"
               unit-name="Philippine Peso"
               unit-symbol="PHP"
               version="1"/>

finance.currency.pkr
--------------------
*an amount of Pakistan Rupees*

.. code-block:: xml

  <object-type name="finance.currency.pkr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Pakistan Rupees"
               data-type="number:currency"
               unit-name="Pakistan Rupee"
               unit-symbol="PKR"
               version="1"/>

finance.currency.pln
--------------------
*an amount of Zlotys*

.. code-block:: xml

  <object-type name="finance.currency.pln"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Zlotys"
               data-type="number:currency"
               unit-name="Zloty"
               unit-symbol="PLN"
               version="1"/>

finance.currency.pyg
--------------------
*an amount of Guaranis*

.. code-block:: xml

  <object-type name="finance.currency.pyg"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Guaranis"
               data-type="number:currency"
               unit-name="Guarani"
               unit-symbol="PYG"
               version="1"/>

finance.currency.qar
--------------------
*an amount of Qatari Rials*

.. code-block:: xml

  <object-type name="finance.currency.qar"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Qatari Rials"
               data-type="number:currency"
               unit-name="Qatari Rial"
               unit-symbol="QAR"
               version="1"/>

finance.currency.ron
--------------------
*an amount of Romanian Leus*

.. code-block:: xml

  <object-type name="finance.currency.ron"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Romanian Leus"
               data-type="number:currency"
               unit-name="Romanian Leu"
               unit-symbol="RON"
               version="1"/>

finance.currency.rsd
--------------------
*an amount of Serbian Dinars*

.. code-block:: xml

  <object-type name="finance.currency.rsd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Serbian Dinars"
               data-type="number:currency"
               unit-name="Serbian Dinar"
               unit-symbol="RSD"
               version="1"/>

finance.currency.rub
--------------------
*an amount of Russian Rubles*

.. code-block:: xml

  <object-type name="finance.currency.rub"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Russian Rubles"
               data-type="number:currency"
               unit-name="Russian Ruble"
               unit-symbol="RUB"
               version="1"/>

finance.currency.rwf
--------------------
*an amount of Rwanda Francs*

.. code-block:: xml

  <object-type name="finance.currency.rwf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Rwanda Francs"
               data-type="number:currency"
               unit-name="Rwanda Franc"
               unit-symbol="RWF"
               version="1"/>

finance.currency.sar
--------------------
*an amount of Saudi Riyals*

.. code-block:: xml

  <object-type name="finance.currency.sar"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Saudi Riyals"
               data-type="number:currency"
               unit-name="Saudi Riyal"
               unit-symbol="SAR"
               version="1"/>

finance.currency.sbd
--------------------
*an amount of Solomon Islands Dollars*

.. code-block:: xml

  <object-type name="finance.currency.sbd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Solomon Islands Dollars"
               data-type="number:currency"
               unit-name="Solomon Islands Dollar"
               unit-symbol="SBD"
               version="1"/>

finance.currency.scr
--------------------
*an amount of Seychelles Rupees*

.. code-block:: xml

  <object-type name="finance.currency.scr"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Seychelles Rupees"
               data-type="number:currency"
               unit-name="Seychelles Rupee"
               unit-symbol="SCR"
               version="1"/>

finance.currency.sdg
--------------------
*an amount of Sudanese Pounds*

.. code-block:: xml

  <object-type name="finance.currency.sdg"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Sudanese Pounds"
               data-type="number:currency"
               unit-name="Sudanese Pound"
               unit-symbol="SDG"
               version="1"/>

finance.currency.sek
--------------------
*an amount of Swedish Kronas*

.. code-block:: xml

  <object-type name="finance.currency.sek"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Swedish Kronas"
               data-type="number:currency"
               unit-name="Swedish Krona"
               unit-symbol="SEK"
               version="1"/>

finance.currency.sgd
--------------------
*an amount of Singapore Dollars*

.. code-block:: xml

  <object-type name="finance.currency.sgd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Singapore Dollars"
               data-type="number:currency"
               unit-name="Singapore Dollar"
               unit-symbol="SGD"
               version="1"/>

finance.currency.shp
--------------------
*an amount of Saint Helena Pounds*

.. code-block:: xml

  <object-type name="finance.currency.shp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Saint Helena Pounds"
               data-type="number:currency"
               unit-name="Saint Helena Pound"
               unit-symbol="SHP"
               version="1"/>

finance.currency.sll
--------------------
*an amount of Leones*

.. code-block:: xml

  <object-type name="finance.currency.sll"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Leones"
               data-type="number:currency"
               unit-name="Leone"
               unit-symbol="SLL"
               version="1"/>

finance.currency.sos
--------------------
*an amount of Somali Shillings*

.. code-block:: xml

  <object-type name="finance.currency.sos"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Somali Shillings"
               data-type="number:currency"
               unit-name="Somali Shilling"
               unit-symbol="SOS"
               version="1"/>

finance.currency.srd
--------------------
*an amount of Surinam Dollars*

.. code-block:: xml

  <object-type name="finance.currency.srd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Surinam Dollars"
               data-type="number:currency"
               unit-name="Surinam Dollar"
               unit-symbol="SRD"
               version="1"/>

finance.currency.ssp
--------------------
*an amount of South Sudanese Pounds*

.. code-block:: xml

  <object-type name="finance.currency.ssp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of South Sudanese Pounds"
               data-type="number:currency"
               unit-name="South Sudanese Pound"
               unit-symbol="SSP"
               version="1"/>

finance.currency.stn
--------------------
*an amount of Dobras*

.. code-block:: xml

  <object-type name="finance.currency.stn"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Dobras"
               data-type="number:currency"
               unit-name="Dobra"
               unit-symbol="STN"
               version="1"/>

finance.currency.svc
--------------------
*an amount of El Salvador Colons*

.. code-block:: xml

  <object-type name="finance.currency.svc"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of El Salvador Colons"
               data-type="number:currency"
               unit-name="El Salvador Colon"
               unit-symbol="SVC"
               version="1"/>

finance.currency.syp
--------------------
*an amount of Syrian Pounds*

.. code-block:: xml

  <object-type name="finance.currency.syp"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Syrian Pounds"
               data-type="number:currency"
               unit-name="Syrian Pound"
               unit-symbol="SYP"
               version="1"/>

finance.currency.szl
--------------------
*an amount of Lilangenis*

.. code-block:: xml

  <object-type name="finance.currency.szl"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Lilangenis"
               data-type="number:currency"
               unit-name="Lilangeni"
               unit-symbol="SZL"
               version="1"/>

finance.currency.thb
--------------------
*an amount of Bahts*

.. code-block:: xml

  <object-type name="finance.currency.thb"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Bahts"
               data-type="number:currency"
               unit-name="Baht"
               unit-symbol="THB"
               version="1"/>

finance.currency.tjs
--------------------
*an amount of Somonis*

.. code-block:: xml

  <object-type name="finance.currency.tjs"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Somonis"
               data-type="number:currency"
               unit-name="Somoni"
               unit-symbol="TJS"
               version="1"/>

finance.currency.tmt
--------------------
*an amount of Turkmenistan New Manats*

.. code-block:: xml

  <object-type name="finance.currency.tmt"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Turkmenistan New Manats"
               data-type="number:currency"
               unit-name="Turkmenistan New Manat"
               unit-symbol="TMT"
               version="1"/>

finance.currency.tnd
--------------------
*an amount of Tunisian Dinars*

.. code-block:: xml

  <object-type name="finance.currency.tnd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Tunisian Dinars"
               data-type="number:currency"
               unit-name="Tunisian Dinar"
               unit-symbol="TND"
               version="1"/>

finance.currency.top
--------------------
*an amount of Pa’angas*

.. code-block:: xml

  <object-type name="finance.currency.top"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Pa&#8217;angas"
               data-type="number:currency"
               unit-name="Pa&#8217;anga"
               unit-symbol="TOP"
               version="1"/>

finance.currency.try
--------------------
*an amount of Turkish Liras*

.. code-block:: xml

  <object-type name="finance.currency.try"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Turkish Liras"
               data-type="number:currency"
               unit-name="Turkish Lira"
               unit-symbol="TRY"
               version="1"/>

finance.currency.ttd
--------------------
*an amount of Trinidad and Tobago Dollars*

.. code-block:: xml

  <object-type name="finance.currency.ttd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Trinidad and Tobago Dollars"
               data-type="number:currency"
               unit-name="Trinidad and Tobago Dollar"
               unit-symbol="TTD"
               version="1"/>

finance.currency.twd
--------------------
*an amount of New Taiwan Dollars*

.. code-block:: xml

  <object-type name="finance.currency.twd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of New Taiwan Dollars"
               data-type="number:currency"
               unit-name="New Taiwan Dollar"
               unit-symbol="TWD"
               version="1"/>

finance.currency.tzs
--------------------
*an amount of Tanzanian Shillings*

.. code-block:: xml

  <object-type name="finance.currency.tzs"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Tanzanian Shillings"
               data-type="number:currency"
               unit-name="Tanzanian Shilling"
               unit-symbol="TZS"
               version="1"/>

finance.currency.uah
--------------------
*an amount of Hryvnias*

.. code-block:: xml

  <object-type name="finance.currency.uah"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Hryvnias"
               data-type="number:currency"
               unit-name="Hryvnia"
               unit-symbol="UAH"
               version="1"/>

finance.currency.ugx
--------------------
*an amount of Uganda Shillings*

.. code-block:: xml

  <object-type name="finance.currency.ugx"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Uganda Shillings"
               data-type="number:currency"
               unit-name="Uganda Shilling"
               unit-symbol="UGX"
               version="1"/>

finance.currency.usd
--------------------
*an amount of US Dollars*

.. code-block:: xml

  <object-type name="finance.currency.usd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of US Dollars"
               data-type="number:currency"
               unit-name="US Dollar"
               unit-symbol="USD"
               version="1"/>

finance.currency.uyu
--------------------
*an amount of Peso Uruguayos*

.. code-block:: xml

  <object-type name="finance.currency.uyu"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Peso Uruguayos"
               data-type="number:currency"
               unit-name="Peso Uruguayo"
               unit-symbol="UYU"
               version="1"/>

finance.currency.uyw
--------------------
*an amount of Unidad Previsionals*

.. code-block:: xml

  <object-type name="finance.currency.uyw"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Unidad Previsionals"
               data-type="number:currency"
               unit-name="Unidad Previsional"
               unit-symbol="UYW"
               version="1"/>

finance.currency.uzs
--------------------
*an amount of Uzbekistan Sums*

.. code-block:: xml

  <object-type name="finance.currency.uzs"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Uzbekistan Sums"
               data-type="number:currency"
               unit-name="Uzbekistan Sum"
               unit-symbol="UZS"
               version="1"/>

finance.currency.ves
--------------------
*an amount of Bolívar Soberanos*

.. code-block:: xml

  <object-type name="finance.currency.ves"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Bol&#237;var Soberanos"
               data-type="number:currency"
               unit-name="Bol&#237;var Soberano"
               unit-symbol="VES"
               version="1"/>

finance.currency.vnd
--------------------
*an amount of Dongs*

.. code-block:: xml

  <object-type name="finance.currency.vnd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Dongs"
               data-type="number:currency"
               unit-name="Dong"
               unit-symbol="VND"
               version="1"/>

finance.currency.vuv
--------------------
*an amount of Vatus*

.. code-block:: xml

  <object-type name="finance.currency.vuv"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Vatus"
               data-type="number:currency"
               unit-name="Vatu"
               unit-symbol="VUV"
               version="1"/>

finance.currency.wst
--------------------
*an amount of Talas*

.. code-block:: xml

  <object-type name="finance.currency.wst"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Talas"
               data-type="number:currency"
               unit-name="Tala"
               unit-symbol="WST"
               version="1"/>

finance.currency.xaf
--------------------
*an amount of CFA Franc BEACs*

.. code-block:: xml

  <object-type name="finance.currency.xaf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of CFA Franc BEACs"
               data-type="number:currency"
               unit-name="CFA Franc BEAC"
               unit-symbol="XAF"
               version="1"/>

finance.currency.xcd
--------------------
*an amount of East Caribbean Dollars*

.. code-block:: xml

  <object-type name="finance.currency.xcd"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of East Caribbean Dollars"
               data-type="number:currency"
               unit-name="East Caribbean Dollar"
               unit-symbol="XCD"
               version="1"/>

finance.currency.xof
--------------------
*an amount of CFA Franc BCEAOs*

.. code-block:: xml

  <object-type name="finance.currency.xof"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of CFA Franc BCEAOs"
               data-type="number:currency"
               unit-name="CFA Franc BCEAO"
               unit-symbol="XOF"
               version="1"/>

finance.currency.xpf
--------------------
*an amount of CFP Francs*

.. code-block:: xml

  <object-type name="finance.currency.xpf"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of CFP Francs"
               data-type="number:currency"
               unit-name="CFP Franc"
               unit-symbol="XPF"
               version="1"/>

finance.currency.xsu
--------------------
*an amount of Sucres*

.. code-block:: xml

  <object-type name="finance.currency.xsu"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Sucres"
               data-type="number:currency"
               unit-name="Sucre"
               unit-symbol="XSU"
               version="1"/>

finance.currency.xua
--------------------
*an amount of ADB Unit of Accounts*

.. code-block:: xml

  <object-type name="finance.currency.xua"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of ADB Unit of Accounts"
               data-type="number:currency"
               unit-name="ADB Unit of Account"
               unit-symbol="XUA"
               version="1"/>

finance.currency.yer
--------------------
*an amount of Yemeni Rials*

.. code-block:: xml

  <object-type name="finance.currency.yer"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Yemeni Rials"
               data-type="number:currency"
               unit-name="Yemeni Rial"
               unit-symbol="YER"
               version="1"/>

finance.currency.zar
--------------------
*an amount of Rands*

.. code-block:: xml

  <object-type name="finance.currency.zar"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Rands"
               data-type="number:currency"
               unit-name="Rand"
               unit-symbol="ZAR"
               version="1"/>

finance.currency.zmw
--------------------
*an amount of Zambian Kwachas*

.. code-block:: xml

  <object-type name="finance.currency.zmw"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Zambian Kwachas"
               data-type="number:currency"
               unit-name="Zambian Kwacha"
               unit-symbol="ZMW"
               version="1"/>

finance.currency.zwl
--------------------
*an amount of Zimbabwe Dollars*

.. code-block:: xml

  <object-type name="finance.currency.zwl"
               display-name-singular="amount"
               display-name-plural="amounts"
               description="an amount of Zimbabwe Dollars"
               data-type="number:currency"
               unit-name="Zimbabwe Dollar"
               unit-symbol="ZWL"
               version="1"/>

