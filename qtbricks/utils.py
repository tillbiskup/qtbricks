"""
utils module of the qtbricks package.
"""

import os

from PySide6 import QtWidgets, QtGui


def image_path(name='', icon_dir='images'):
    """
    Return full path to a given image.

    Images, such as icons, are used in several places in GUIs, but are
    usually stored in a separate directory. Hence, a generic function
    returning the full path is both, convenient and modular.

    If the internal organisation of images changes, only this code needs to
    be adapted.

    Parameters
    ----------
    name : :class:`str`
        Name of the icon

    icon_dir : :class:`str`
        Directory containing the icons

        Default: "images"

    Returns
    -------
    path : :class:`str`
        Full path to the icon
    """
    basedir = os.path.dirname(__file__)
    path = os.path.join(basedir, icon_dir, name)
    return path


def create_button(text="", slot=None, shortcut=None, icon=None, checkable=False,
                  tooltip=None):
    """
    Conveniently create a button.

    Parameters
    ----------
    text : :class:`str`
        The text appearing on the button.

        In case you provide both, icon (see below) and text, both are
        displayed. If you intend to only present an icon, set the text to an
        empty string.

        Default: empty

    slot : :class:``
        The slot to connect to the button.

    shortcut : :class:`str`
        The keyboard shortcut used for the action connected to the button.

        Default: empty

    icon : class:`str`
        The name of the icon file to be used.

        If empty, no icon will be displayed.

        For enhanced modularity, do *not* provide paths, but only icon file
        names, as the full path will get looked up using the
        :func:`icon_path` function.

    checkable : :class:`bool`
        Whether the button is checkable, *i.e.*, displays its current state.

    tooltip : class:`str`
        Tooltip to be displayed for the button.

        Sensible tooltips go a long way towards a user-friendly GUI.

    Returns
    -------
    button : :class:`QtWidgets.QPushButton`

    """
    button = QtWidgets.QPushButton(text)
    if icon:
        button.setIcon(QtGui.QIcon(image_path(icon)))
    if shortcut:
        button.setShortcut(shortcut)
    if tooltip:
        button.setToolTip(tooltip)
    if slot:
        button.pressed.connect(slot)
    if checkable:
        button.setCheckable(True)
    return button


def make_buttons_in_group_uncheckable(buttongroup):
    """
    Allow all buttons in exclusive button group to be unchecked.

    By default, an exclusive button group does not allow to uncheck all
    buttons by clicking the selected button, but only to select an
    alternative button, once one button has been clicked.

    Parameters
    ----------
    buttongroup : :class:`QtWidgets.QButtonGroup`
        Button group to operate on

    """
    buttongroup.buttonPressed.connect(
        lambda button: button.group().setExclusive(not button.isChecked())
    )
    buttongroup.buttonClicked.connect(
        lambda button: button.group().setExclusive(True)
    )
