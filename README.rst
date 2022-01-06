Development Toolset
===================

Package requirements
~~~~~~~~~~~~~~~~~~~~
- invoke
- ipython

Extra requirements for testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- coverage
- flake8
- pytest
- pytest-cov

Installation instructions
-------------------------

Install package:

    -  From source dir:

        .. code:: console

            $ pip install -e .
        ..

    -  From package archive:

        .. code:: console

            $ pip install toolset-X.Y.Z.tar.gz
        ..

    -  From pypi index (if it exist there)

        .. code:: console

            $ pip install toolset --index-url http://pypi.url.domain
        ..

Usage
-----

From command line:

    - Available commands:

        .. code:: console

            $ toolset -l
        ..

    - Merge log files:

        .. code:: console

            $ toolset logs.merge --file=log_1.log --file=log_2.log --level=critical
        ..

Run tests
---------

-  From source dir:

        .. code:: console

            $ pip install -e .[test]
            $ pytest
        ..