import sys

if 'PyQt5' in sys.modules:
    # PyQt5
    from PyQt5 import QtGui, QtWidgets, QtCore
    from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
else:
    # PySide2
    from PySide2 import QtGui, QtWidgets, QtCore
    from PySide2.QtCore import Signal, Slot


class LeftPanelView(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(LeftPanelView, self).__init__(parent)
        self._initUI()

    def _initUI(self):
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        offset = QtCore.QSettings().value("ui_margin_offset", -4)
        self.setContentsMargins(offset, offset, 2 * offset, offset)
