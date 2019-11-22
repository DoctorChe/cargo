import sys

from cargo.ui.views.TasksListView import TasksListView

if 'PyQt5' in sys.modules:
    # PyQt5
    from PyQt5 import QtGui, QtWidgets, QtCore
    from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
else:
    # PySide2
    from PySide2 import QtGui, QtWidgets, QtCore
    from PySide2.QtCore import Signal, Slot


class RightPanelView(QtWidgets.QWidget):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self._initUI()

    def _initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        self.tasks_list_view = TasksListView(self)
        offset = QtCore.QSettings().value("ui_margin_offset", -4)
        self.setContentsMargins(2 * offset, offset, offset, offset)
        layout.addWidget(self.tasks_list_view)
        self.setLayout(layout)
