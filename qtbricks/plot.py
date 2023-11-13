"""
Plot widget for including Matplotlib plots in a GUI.

Graphical representations of data are an often-found use case in scientific
GUIs. The de-facto framework for such plotting in Python in Matplotlib,
hence this widget to include a Matplotlib figure into a Qt GUI.


General characteristics and intended purpose
============================================

Ideally, the programmer dealing with the actual plotting tasks does not need
to care in any way where the plot ends up, hence the respective figure and
axes objects are exposed as public attributes of the widget.

Plot windows exposed to users for interaction should typically provide a
numer of functions, such as zooming and panning. While the default
Matplotlib windows come with this functionality built-in, it is not
necessarily intuitive and lacks, e.g., support of the mouse wheel for
zooming. Hence, the plot widget implemented here aims at bridging this gap.


How to use the Plot widget in own GUIs?
=======================================

A rather minimal (and not very useful, though educational) example,
including the :class:`FileBrowser` as only widget of a main window:

.. code-block::

    import sys

    from PySide6 import QtWidgets

    import plot


    class MainWindow(QtWidgets.QMainWindow):

        def __init__(self):
            super().__init__()

            widget = plot.Plot()
            self.setCentralWidget(widget)

            import numpy as np

            t = np.linspace(0, 4*np.pi, 501)
            widget.axes.plot(t, np.sin(t), ".")

            self.show()


    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        w = MainWindow()
        app.exec()


Of course, an import statement buried in a class is nothing you should
ever do in productive code. Nevertheless, it shows in minimalistic fashion
how to use the :class:`Plot` widget. As you can see, the figure and axes
properties are exposed as :attr:`Plot.figure` and :attr:`Plot.axes`,
and as these are the respective Matplotlib objects, they behave exactly as
expected.


Notes for developers
====================

TBD

.. todo::
    Implement mouse wheel for zooming (& panning) in Matplotlib canvas.

    https://stackoverflow.com/questions/11551049/


Module documentation
====================

"""

import sys

# Import PySide6 before matplotlib
from PySide6 import QtWidgets

from matplotlib import figure, widgets
from matplotlib.backends import backend_qtagg as backend

import qtbricks.utils as utils


class Plot(QtWidgets.QWidget):
    """
    Plot widget for including Matplotlib plots in a GUI.

    Besides the actual figure canvas containing the figure, a series of
    buttons is attached to the top, similar to the default toolbar of a
    Matplotlib window.

    As the widget exposes two public attributes, :attr:`figure` and
    :attr:`axes`, plotting should be fairly straight-forward and basically
    identical to other plots.

    If you need to change the axes, *e.g.* for multiple axes in a figure,
    this can be achieved by simply clearing the figure and creating new axes
    via the :meth:`matplotlib.figure.Figure.subplots` method:

    .. code-block::

        widget = Plot()
        widget.figure.clf()
        axes = widget.figure.subplots(2, 1)

        axes[0].plot(t, np.sin(t), ".")
        axes[1].plot(t, np.cos(t), ".")


    Attributes
    ----------
    figure : :class:`matplotlib.figure.Figure`
        Matplotlib figure containing the actual plot

    axes : :class:`matplotlib.axes.Axes`
        Matplotlib axes for plotting data
    """

    def __init__(self):
        super().__init__()
        figure_canvas = _FigureCanvas()
        self.figure = figure_canvas.figure
        self.axes = figure_canvas.axes

        self._cursor = None

        self._setup_ui(figure_canvas)

    def _setup_ui(self, figure_canvas):
        mpl_toolbar = backend.NavigationToolbar2QT(figure_canvas, None)
        home_button = utils.create_button(
            icon="house.svg",
            shortcut="h",
            tooltip="Reset plot to default settings",
            slot=mpl_toolbar.home,
        )
        back_button = utils.create_button(
            icon="backward-step.svg",
            tooltip="Undo last change",
            slot=mpl_toolbar.back,
        )
        forward_button = utils.create_button(
            icon="forward-step.svg",
            tooltip="Redo last change",
            slot=mpl_toolbar.forward,
        )
        # Button group
        pan_button = utils.create_button(
            icon="arrows-up-down-left-right.svg",
            shortcut="p",
            tooltip="Pan plot",
            slot=mpl_toolbar.pan,
            checkable=True,
        )
        zoom_button = utils.create_button(
            icon="magnifying-glass.svg",
            shortcut="z",
            tooltip="Zoom plot",
            slot=mpl_toolbar.zoom,
            checkable=True,
        )
        pan_zoom_group = QtWidgets.QButtonGroup(self)
        pan_zoom_group.addButton(pan_button)
        pan_zoom_group.addButton(zoom_button)
        utils.make_buttons_in_group_uncheckable(pan_zoom_group)
        # /Button group
        self._crosshair_button = utils.create_button(
            icon="plus.svg",
            shortcut="x",
            tooltip="Show crosshair cursor",
            slot=self._crosshair_button_action,
            checkable=True,
        )
        subplots_button = utils.create_button(
            icon="chart-line.svg",
            tooltip="Configure subplots",
            slot=mpl_toolbar.configure_subplots,
        )
        customise_button = utils.create_button(
            icon="sliders.svg",
            tooltip="Customise plot appearance",
            slot=mpl_toolbar.edit_parameters,
        )
        save_button = utils.create_button(
            icon="floppy-disk.svg",
            tooltip="Save plot",
            slot=mpl_toolbar.save_figure,
        )

        controls_layout = QtWidgets.QHBoxLayout()
        controls_layout.addWidget(home_button)
        controls_layout.addWidget(back_button)
        controls_layout.addWidget(forward_button)
        controls_layout.addWidget(zoom_button)
        controls_layout.addWidget(pan_button)
        controls_layout.addWidget(self._crosshair_button)
        controls_layout.addWidget(subplots_button)
        controls_layout.addWidget(customise_button)
        controls_layout.addWidget(save_button)
        controls_layout.addStretch()
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(controls_layout)
        layout.addWidget(figure_canvas)
        self.setLayout(layout)

    def _crosshair_button_action(self):
        if self._crosshair_button.isChecked():
            for hline in self._cursor.hlines:
                hline.remove()
            for vline in self._cursor.vlines:
                vline.remove()
            self._cursor = None
            self.figure.canvas.restore_region(self._background)
            self.figure.canvas.blit(self.figure.bbox)
        else:
            self._background = \
                self.figure.canvas.copy_from_bbox(self.figure.bbox)
            if not self._cursor:
                self._cursor = widgets.MultiCursor(
                    None, self.axes, useblit=False, horizOn=True, vertOn=True,
                    color='red', linewidth=1,
                )


class _FigureCanvas(backend.FigureCanvasQTAgg):
    """
    Figure canvas containing the Matplotlib figure for use within Qt GUIs.


    Attributes
    ----------
    figure : :class:`matplotlib.figure.Figure`
        Matplotlib figure containing the actual plot

    axes : :class:`matplotlib.axes.Axes`
        Matplotlib axes for plotting data

    """

    def __init__(self):
        self.figure = figure.Figure()  # figsize=(width, height), dpi=dpi
        self.axes = self.figure.add_subplot(111)
        super().__init__(self.figure)


class _MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        widget = Plot()
        self.setCentralWidget(widget)

        import numpy as np

        t = np.linspace(0, 4*np.pi, 501)
        widget.axes.plot(t, np.sin(t), ".")

        widget.figure.clf()

        widget.axes = widget.figure.subplots(2, 1)
        widget.axes[0].plot(t, np.sin(t), ".")

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = _MainWindow()
    app.exec()
