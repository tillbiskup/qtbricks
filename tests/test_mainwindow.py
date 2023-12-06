import unittest

from PySide6 import QtCore, QtWidgets

from qtbricks import mainwindow


class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.app = (
            QtWidgets.QApplication.instance() or QtWidgets.QApplication()
        )
        self.window = mainwindow.MainWindow()
        self.addCleanup(self.release_qt_resources)

    def release_qt_resources(self):
        self.window.deleteLater()
        self.app.sendPostedEvents(event_type=QtCore.QEvent.DeferredDelete)
        self.app.processEvents()

    def test_instantiate_class(self):
        pass
