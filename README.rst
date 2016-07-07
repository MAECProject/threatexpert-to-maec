ThreatExpert XML -> MAEC XML Converter Script
=============================================

Copyright (c) 2015 - The MITRE Corporation

BY USING THE THREATEXPERT TO MAEC SCRIPT, YOU SIGNIFY YOUR ACCEPTANCE OF THE TERMS AND 
CONDITIONS OF USE.  IF YOU DO NOT AGREE TO THESE TERMS, DO NOT USE THE SCRIPT.
For more information, please refer to the LICENSE.txt file.

v0.99 - BETA

Updated 02/10/2014

Overview
--------

The software has two components: a stand-alone module (in ``threatexpert_to_maec/``) and a command-line script that uses the module (``threatexpert_parser.py``). The software generates a MAEC Package from a ThreatExpert XML file. The module can also accept an MD5 hash of a known binary file, which it uses to query the ``threatexpert.com`` server to fetch the report for the binary.

Compatible with MAEC Schema v4.1 & Cyber Observable eXpression (CybOX™) 2.1.

* MAEC - http://maecproject.github.io/
* ThreatExpert - http://www.threatexpert.com
* CybOX - http://cyboxproject.github.io/

Included Files
--------------

* ``README.rst``: this file.

* ``threatexpert_to_maec.py``: the ThreatExpert XML to MAEC XML Python converter script.

* ``LICENSE.txt``: the terms of use for this script.

* ``threatexpert_to_maec/``: package for transforming ThreatExpert reports to MAEC and fetching reports from threatexpert.com

  - ``__init__.py`` - defines the module functions, see "Module Usage" below

  - ``threatexpert.py``: the ThreatExpert XML-to-Python bindings

  - ``threatexpert_parser.py``: the ThreatExpert to MAEC parser class, which does most of the conversion work.

Dependencies
------------

This code has been developed and tested under Python 2.7.x and so may not be compatible with Python 3.x.

There are three dependencies for this script:

1. The Python ``lxml`` library  >= 3.2.x, http://lxml.de/
2. The ``python-maec`` library  >= v4.1.0.9: https://pypi.python.org/pypi/maec
3. The ``python-cybox`` library >= v2.1.0.8: https://pypi.python.org/pypi/cybox

Script Usage
------------

The input ThreatExpert file or directory should be specified as the first argument, and the output file or directory should be specified as the second argument.

The script also supports the following optional command line parameters:

* ``--deduplicate``, ``-dd``: deduplicate objects in MAEC output

* ``--dereference``, ``-dr``: dereference the MAEC output

* ``--normalize``, ``-n``: normalize the MAEC output

* ``--verbose``, ``-v``: print verbose error output (tracebacks)

To use the script, run the following command::

    python threatexpert_to_maec.py <input ThreatExpert file/dir> <output MAEC file/dir> <flags>

Module Usage
------------

The module exposes several functions:

* ``generate_package_from_report_filepath`` - given a filepath to a ThreatExpert report, return a python-maec Pacakge object

* ``generate_package_from_report_string`` - given a ThreatExpert report XML string, return a python-maec Pacakge object

* ``generate_package_from_md5`` - given an MD5 string, return a python-maec Pacakge object (using MD5 lookup on `threatexpert.com``)

* ``generate_package_from_binary_filepath`` - given an binary filepath, return a python-maec Pacakge object (looks up the report from ``threatexpert.com`` by the binary's MD5)

* ``set_proxies`` - optionally called to supply proxy information to the package; supplied as a dictionary like ``{ "http": "http://example.com:80", ... }``

About MAEC
------------

Malware Attribute Enumeration and Characterization (MAEC™) is a standardized language for sharing structured information about malware based upon attributes such as behaviors, artifacts, and attack patterns.

The goal of the MAEC (pronounced "mike") effort is to provide a basis for transforming malware research and response. MAEC aims to eliminate the ambiguity and inaccuracy that currently exists in malware descriptions and to reduce reliance on signatures. In this way, MAEC seeks to improve human-to-human, human-to-tool, tool-to-tool, and tool-to-human communication about malware; reduce potential duplication of malware analysis efforts by researchers; and allow for the faster development of countermeasures by enabling the ability to leverage responses to previously observed malware instances. The MAEC Language enables correlation, integration, and automation.

Please visit the MAEC website at http://maecproject.github.io/ for more information about the MAEC Language.

Getting Help
------------

Join the public MAEC Community Email Discussion List at https://maec.mitre.org/community/discussionlist.html.

Email the MAEC Developers at maec@mitre.org.
