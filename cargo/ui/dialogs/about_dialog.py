"""Окно о программе"""
from PyQt5 import QtWidgets, QtCore, QtGui

from cargo.ui.dialogs.ui_about_dialog import Ui_AboutDialog


class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.Window)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        # self.ui.label_logo.setPixmap(QtGui.QPixmap("logo.png"))
