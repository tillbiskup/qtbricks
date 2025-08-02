=========
Changelog
=========

This page contains a summary of changes between the official qtbricks releases. Only the biggest changes are listed here. A complete and detailed log of all changes is available through the `GitHub Repository Browser <https://github.com/tillbiskup/qtbricks>`_.


Version 0.1.0
=============

Not yet released

* First public release

* ...


Version 0.1.0-rc3
=================

Not yet released

* Third public pre-release


New features
------------

* New module :mod:`qtbricks.widgets` containing small Qt widgets for general use with Qt GUIs.


Version 0.1.0-rc2
=================

Released 2024-01-15

* Second public pre-release


New features
------------

* New widget: Help-About window

  * Modular general information about a given package
  * Reads most metadata from the package ``setup.py``

* Plot widget

  * Display grid

* New module: :mod:`qtbricks.testing`

  * Testing-related helper functionality

* Utils

  * :class:`qtbricks.utils.IntValidator`: Integer validator actually fixing input that is beyond the boundaries.

* Implementation

  * Start with proper unit tests
  * Code formatting using Black


Version 0.1.0-rc1
=================

Released 2023-11-18

* First public pre-release

* Basic versions of the following widgets:

  * File browser
  * Plot

* Main window with basic functionality
