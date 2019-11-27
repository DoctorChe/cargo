from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot, Qt
from PyQt5.QtWidgets import QPushButton


class LeftPanelView(QtWidgets.QWidget):

    btn_clicked = Signal(int)

    def __init__(self, parent=None):
        super(LeftPanelView, self).__init__(parent)
        self._initUI()

    def _initUI(self):
        layout = QtWidgets.QVBoxLayout()
        # self.stackedWidget = QStackedWidget()
        # layout.addWidget(self.stackedWidget, alignment=Qt.AlignTop)

        # put any widgets here
        # self.label = QLabel('Staff')
        # layout.addWidget(self.label, alignment=Qt.AlignTop)
        self.button = QPushButton('Staff')
        self.button.page = 0
        self.button.clicked.connect(self.btn_staff_clicked)
        layout.addWidget(self.button, alignment=Qt.AlignTop)

        self.setLayout(layout)

        offset = QtCore.QSettings().value("ui_margin_offset", -4)
        self.setContentsMargins(offset, offset, 2 * offset, offset)

    def btn_staff_clicked(self):
        self.button = self.sender()
        # self.stackedWidget.setCurrentIndex(self.button.page - 1)
        self.btn_clicked.emit(self.button.page)
