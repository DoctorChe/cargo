# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(451, 167)
        self.label = QtWidgets.QLabel(AboutDialog)
        self.label.setGeometry(QtCore.QRect(160, 20, 221, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_version = QtWidgets.QLabel(AboutDialog)
        self.label_version.setGeometry(QtCore.QRect(160, 50, 211, 17))
        self.label_version.setObjectName("label_version")
        self.label_description = QtWidgets.QLabel(AboutDialog)
        self.label_description.setGeometry(QtCore.QRect(160, 70, 361, 61))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_description.setFont(font)
        self.label_description.setTextFormat(QtCore.Qt.AutoText)
        self.label_description.setObjectName("label_description")
        self.label_copiright = QtWidgets.QLabel(AboutDialog)
        self.label_copiright.setGeometry(QtCore.QRect(160, 130, 211, 17))
        self.label_copiright.setObjectName("label_copiright")
        self.widget_logo = QtWidgets.QWidget(AboutDialog)
        self.widget_logo.setGeometry(QtCore.QRect(10, 10, 141, 141))
        self.widget_logo.setObjectName("widget_logo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_logo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_logo = QtWidgets.QVBoxLayout()
        self.verticalLayout_logo.setObjectName("verticalLayout_logo")
        self.label_logo = QtWidgets.QLabel(self.widget_logo)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.verticalLayout_logo.addWidget(self.label_logo)
        self.horizontalLayout.addLayout(self.verticalLayout_logo)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "О программе"))
        self.label.setText(_translate("AboutDialog", "CompanyStatistics"))
        self.label_version.setText(_translate("AboutDialog", "Версия 0.0.1"))
        self.label_description.setText(_translate("AboutDialog",
                                                  "<html><head/><body><p>Программа для учета грузоперевозок</p></body></html>"))
        self.label_copiright.setText(_translate("AboutDialog", "Copiright (C) 2019"))


