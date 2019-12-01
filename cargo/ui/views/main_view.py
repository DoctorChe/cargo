from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot, Qt

from cargo.ui.views.central_panel_view import CentralPanelView


class MainView(QtWidgets.QMainWindow):
    closeEventSignal = Signal(QtGui.QCloseEvent)

    def __init__(self, parent=None):
        super(MainView, self).__init__(parent, flags=Qt.WindowFlags())
        self._init_ui()

    def show(self):
        super(MainView, self).show()

    def hide(self):
        super(MainView, self).hide()

    def _init_ui(self):
        self.setWindowTitle('CompanyStatistics')

        self.central_panel = CentralPanelView(parent=None)
        self.setCentralWidget(self.central_panel)

        self.resize(870, 650)

    def closeEvent(self, closeEvent):
        super(MainView, self).closeEvent(closeEvent)
        self.closeEventSignal.emit(closeEvent)
