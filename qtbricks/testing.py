"""
Testing-related helper functionality of the qtbricks package.

GUIs should be tested, as every code. However, testing GUIs and widgets is
somewhat more complicated and often involves "faking" interaction with the
different widgets.

In case of Qt, even setting up a test in a way that allows for testing any
GUI-related stuff needs a bit of additional knowledge.

This module contains a growing series of helper classes and functions
designed to make your test code simpler and easier to read.
"""

from PySide6 import QtCore, QtTest


def qtest_enter_text(widget=None, text=""):
    """
    Convenience function to enter text in a QLineEdit widget.

    When testing GUI widgets, you sometimes need to enter text into a line
    edit widget. However, entering/replacing text in such a widget is a
    three-step process:

    #. Clear the current text.
    #. Enter the text.
    #. Press the return key to fire the correct signals.

    For convenience, this function takes care of all three steps.

    Parameters
    ----------
    widget : :class:`PySide6.QtWidgets.QLineEdit`
        Widget to enter text into.

    text : :class:`str`
        Text to enter into the widget.

    """
    widget.clear()
    QtTest.QTest.keyClicks(widget, text)
    QtTest.QTest.keyPress(widget, QtCore.Qt.Key.Key_Return)
