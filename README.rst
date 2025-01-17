Bankruptcy
==========

A bankruptcy document parser.

Notes
==========

Bankruptcy is an open source repository to extract content from bankruptcy documents
It was built for use with Courtlistener.com.

Its main goal is to convert bankruptcy documents into readable JSON data.

Further development is intended and all contributors, corrections and additions are welcome.

Background
==========

This was built to help extract content from bankruptcy documents.

Documents
=========

We currently support the following documents in a voluntary petition.

- Bankruptcy Official Form 106 A/B (Property)
- Bankruptcy Official Form 106 D (Secured Creditors)
- Bankruptcy Official Form 106 E/F (Unsecured Creditors)
- Bankruptcy Official Form 106Sum (Statistics)

TODOs
=====

- B 101 (Official Form 101)
- B2030 (Form 2030) (12/15)
- 521.05 (12/1/08)
- Official Form 106C
- Official Form 106G
- Official Form 106H
- Official Form 106I
- Official Form 106J
- Official Form 106Dec
- Official Form 107


Quickstart
==========

    from bankruptcy import extract_all
    results = extract_all(filepath=filepath)

will return a dictionary of the forms (if found) and the contents of the document.


Some Notes
==========

This tool relies heavily on PDFPlumber.

Somethings to keep in mind this parser has been tested only on digital PDFs
from recent court filings (ie 2018 and earlier).  This parser does not work on scanned
bankruptcy documents and was built and tested on documents from the Pacific Northwest.


Installation
===============

Installing bankruptcy is easy.

::

    pip install bankruptcy

Or install the latest dev version from github

::

    pip install git+https://github.com/freelawproject/bankruptcy.git@master


Testing
==========

    python3 -m unittest test.tests

Future
======

1) Continue to improve and add documents for extraction.
2) Future updates

Deployment
==========

Tag a release with a similar format v1.0.0, update setup.py and push to master.

License
==========

This repository is available under the permissive BSD license, making it easy and safe to incorporate in your own libraries.

Pull and feature requests welcome. Online editing in GitHub is possible (and easy!)
