========
qtbricks
========

*Python Qt components: widgets and utils, focussing on scientific GUIs.*

Welcome! This is the documentation for qtbricks, a Python package collecting a growing series of "real-world" GUI widgets and related tools written with and for PySide6, the official Python bindings for Qt6.

Do you want or need to create complex GUIs with Python and Qt but don't want to spend too much time reimplementing seemingly basic widgets and functionality? Are you overwhelmed by the complexity of GUI programming and just want to focus on the actual tasks that need to get done? So do we, and that's how qtbricks was born. Separate the GUI from the business logic in your code, provide a series of high-level GUI widgets for (admittedly complex) standard tasks, focus on as readable and as Pythonic code as possible.


Features
========

A list of features:

* Highly modular code: each widget is as self-contained as possible

* User-friendly: obvious behaviour, no surprises, hints (via tooltips) included

* Separation of concerns: widgets handle the GUI stuff and expose a programmatic API

* Designed with code readability in mind


And to make it even more convenient for users and future-proof:

* Open source project written in Python (>= 3.7)

* Developed fully test-driven (well, not yet...)

* Extensive user and API documentation



.. warning::
  qtbricks is currently under active development and still considered in Beta development state. Therefore, expect frequent changes in features and public APIs that may break your own code. Nevertheless, feedback as well as feature requests are highly welcome.


Installation
============

To install the qtbricks package on your computer (sensibly within a Python virtual environment), open a terminal (activate your virtual environment), and type in the following:

.. code-block:: bash

    pip install qtbricks


License
=======

This program is free software: you can redistribute it and/or modify it under the terms of the **BSD License**.



.. toctree::
   :maxdepth: 2
   :caption: User Manual:
   :hidden:

   audience
   usecases
   installing

.. toctree::
   :maxdepth: 2
   :caption: Developers:
   :hidden:

   people
   developers
   changelog
   roadmap
   api/index

