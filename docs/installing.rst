Installation
============

Installing the qtbricks package is as simple as installing any other Python package, as qtbricks is available from the `Python Package Index (PyPI) <https://www.pypi.org/>`_. Simply open a terminal on your computer and type:

.. code-block:: bash

    pip install qtbricks

This will install the qtbricks package (and all its dependencies) on your computer.

Of course, you need to have Python (and pip) installed before you can use the above command, and it is always advisable to install packages in a **virtual environment** of their own.

Hence, a more thorough sequence of events would be:

#. Install Python (if it is not already installed on your system).

#. Create a Python virtual environment for qtbricks.

#. Activate the newly created virtual environment.

#. Install qtbricks therein, using the above command.

A few details for all these steps are given below.


Installing Python
-----------------

For how to install Python on your system, see the `official documentation <https://wiki.python.org/moin/BeginnersGuide/Download>`_. Linux users: you will most certainly have Python installed already.


Create a Python virtual environment
-----------------------------------

It is good practice to always use virtual environments when working with Python. One reason: On some operating systems, crucial tasks depend on Python, and installing Python packages globally may interfere with the system.

The good news: Creating Python virtual environments is fairly simple:

.. code-block:: bash

    python3 -m venv qtbricks

This will create a Python virtual environment named ``qtbricks`` in the current directory. Of course, you can give your virtual environment any name you like. However, be careful with spaces and special characters, depending on your system.


Activate the newly created virtual environment
----------------------------------------------

A Python virtual environment needs to be activated. This is usually done using the following command:

.. code-block:: bash

    source qtbricks/bin/activate

Assuming in this case that your virtual environment is called ``qtbricks`` and that you are in the same path where you just created your virtual environment.

Deactivating is simple as well, once you are done. Either close the terminal, or issue the command ``deactivate``.


Install qtbricks
----------------

Once you activated your virtual environment where you want to install the qtbricks package in, proceed as given above:

.. code-block:: bash

    pip install qtbricks

This will download the qtbricks package from the `Python Package Index (PyPI) <https://www.pypi.org/>`_ and install it locally. All dependencies will be installed as well.


.. note::

    The above instructions assume a fairly standard Python installation using pip. Of course, there are other Python distributions available as well, such as conda. If you are using such a Python distribution, pip should be available as well. However, in case of problems consult the documentation of your respective Python distribution for details.

