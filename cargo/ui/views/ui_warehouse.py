# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warehouse.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 593)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.tw_warehouse = QtWidgets.QTableWidget(Form)
        self.tw_warehouse.setObjectName("tw_warehouse")
        self.tw_warehouse.setColumnCount(0)
        self.tw_warehouse.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tw_warehouse)
        self.verticalLayout_2.setStretch(1, 3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pb_create_warehouse = QtWidgets.QPushButton(Form)
        self.pb_create_warehouse.setObjectName("pb_create_warehouse")
        self.verticalLayout_3.addWidget(self.pb_create_warehouse)
        self.pb_update_warehouse = QtWidgets.QPushButton(Form)
        self.pb_update_warehouse.setObjectName("pb_update_warehouse")
        self.verticalLayout_3.addWidget(self.pb_update_warehouse)
        self.pb_delete_warehouse = QtWidgets.QPushButton(Form)
        self.pb_delete_warehouse.setObjectName("pb_delete_warehouse")
        self.verticalLayout_3.addWidget(self.pb_delete_warehouse)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.le_address = QtWidgets.QLineEdit(Form)
        self.le_address.setObjectName("le_address")
        self.verticalLayout_3.addWidget(self.le_address)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.cb_city = QtWidgets.QComboBox(Form)
        self.cb_city.setObjectName("cb_city")
        self.verticalLayout_3.addWidget(self.cb_city)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Список складов"))
        self.pb_create_warehouse.setText(_translate("Form", "Создать"))
        self.pb_update_warehouse.setText(_translate("Form", "Обновить"))
        self.pb_delete_warehouse.setText(_translate("Form", "Удалить"))
        self.label.setText(_translate("Form", "Адрес"))
        self.label_2.setText(_translate("Form", "Город"))
