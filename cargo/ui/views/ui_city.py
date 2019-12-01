# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'city.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(673, 493)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.tw_city = QtWidgets.QTableWidget(Form)
        self.tw_city.setObjectName("tw_city")
        self.tw_city.setColumnCount(0)
        self.tw_city.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tw_city)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tw_warehouses = QtWidgets.QTableWidget(Form)
        self.tw_warehouses.setObjectName("tw_warehouses")
        self.tw_warehouses.setColumnCount(0)
        self.tw_warehouses.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tw_warehouses)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(3, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pb_create_city = QtWidgets.QPushButton(Form)
        self.pb_create_city.setObjectName("pb_create_city")
        self.verticalLayout_3.addWidget(self.pb_create_city)
        self.pb_update_city = QtWidgets.QPushButton(Form)
        self.pb_update_city.setObjectName("pb_update_city")
        self.verticalLayout_3.addWidget(self.pb_update_city)
        self.pb_delete_city = QtWidgets.QPushButton(Form)
        self.pb_delete_city.setObjectName("pb_delete_city")
        self.verticalLayout_3.addWidget(self.pb_delete_city)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.le_name = QtWidgets.QLineEdit(Form)
        self.le_name.setObjectName("le_name")
        self.verticalLayout_3.addWidget(self.le_name)
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
        self.label_6.setText(_translate("Form", "Список городов"))
        self.label.setText(_translate("Form", "Список складов"))
        self.pb_create_city.setText(_translate("Form", "Создать"))
        self.pb_update_city.setText(_translate("Form", "Обновить"))
        self.pb_delete_city.setText(_translate("Form", "Удалить"))
        self.label_5.setText(_translate("Form", "Название"))
