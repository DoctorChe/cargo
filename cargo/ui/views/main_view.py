from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot, Qt

from cargo.ui.views.left_panel_view import LeftPanelView
from cargo.ui.views.right_panel_view import RightPanelView


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

        # self.splitter = QtWidgets.QSplitter()
        # self.splitter.setHandleWidth(1)
        #
        # self.left_panel = LeftPanelView(self.splitter)
        # self.right_panel = RightPanelView(self.splitter)
        #
        # self.setCentralWidget(self.splitter)

        self.right_panel = RightPanelView(parent=None)
        self.setCentralWidget(self.right_panel)

        self.resize(870, 650)
        # self.splitter.setSizes([300, 550])

    def closeEvent(self, closeEvent):
        super(MainView, self).closeEvent(closeEvent)
        self.closeEventSignal.emit(closeEvent)
