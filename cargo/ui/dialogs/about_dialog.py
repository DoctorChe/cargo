"""Окно о программе"""
import os

from PyQt5 import QtWidgets, QtCore, QtGui

from cargo.ui.dialogs.ui_about_dialog import Ui_AboutDialog
from cargo.utils.config import BASE_DIR


class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.Window)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.ui.label_logo.setPixmap(QtGui.QPixmap(os.path.join(BASE_DIR, 'ui', 'resources', 'logo.png')))
