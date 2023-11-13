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

from matplotlib import figure
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg, NavigationToolbar2QT,
)

import qtbricks.utils as utils


class Plot(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        figure_canvas = _FigureCanvas()
        self.figure = figure_canvas.figure
        self.axes = figure_canvas.axes

        mpl_toolbar = NavigationToolbar2QT(figure_canvas, None)

        home_button = utils.add_button(
            icon="house.svg",
            tooltip="Reset plot to default settings",
            slot=mpl_toolbar.home
        )
        back_button = utils.add_button(
            icon="backward-step.svg",
            tooltip="Undo last change",
            slot=mpl_toolbar.back
        )
        forward_button = utils.add_button(
            icon="forward-step.svg",
            tooltip="Redo last change",
            slot=mpl_toolbar.forward
        )
        pan_button = utils.add_button(
            icon="arrows-up-down-left-right.svg",
            tooltip="Pan plot",
            slot=mpl_toolbar.pan
        )
        zoom_button = utils.add_button(
            icon="magnifying-glass.svg",
            tooltip="Zoom plot",
            slot=mpl_toolbar.zoom
        )
        subplots_button = utils.add_button(
            icon="chart-line.svg",
            tooltip="Configure subplots",
            slot=mpl_toolbar.configure_subplots
        )
        customise_button = utils.add_button(
            icon="sliders.svg",
            tooltip="Customise plot appearance",
            slot=mpl_toolbar.edit_parameters
        )
        save_button = utils.add_button(
            icon="floppy-disk.svg",
            tooltip="Save plot",
            slot=mpl_toolbar.save_figure
        )
        detach_button = utils.add_button(
            icon="share-from-square.svg",
            tooltip="Detach plot (open additional plot window)",
            slot=self._default_button_action
        )

        controls_layout = QtWidgets.QHBoxLayout()
        controls_layout.addWidget(home_button)
        controls_layout.addWidget(back_button)
        controls_layout.addWidget(forward_button)
        controls_layout.addWidget(zoom_button)
        controls_layout.addWidget(pan_button)
        controls_layout.addWidget(subplots_button)
        controls_layout.addWidget(customise_button)
        controls_layout.addWidget(save_button)
        controls_layout.addStretch()
        controls_layout.addWidget(detach_button)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(controls_layout)
        layout.addWidget(figure_canvas)
        self.setLayout(layout)

    def _default_button_action(self):
        pass


class _FigureCanvas(FigureCanvasQTAgg):

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

        axes = widget.figure.subplots(2, 1)
        axes[0].plot(t, np.sin(t), ".")

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = _MainWindow()
    app.exec()
