# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff.ui'
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
        self.tw_staff = QtWidgets.QTableWidget(Form)
        self.tw_staff.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_staff.setAlternatingRowColors(True)
        self.tw_staff.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_staff.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tw_staff.setColumnCount(4)
        self.tw_staff.setObjectName("tw_staff")
        self.tw_staff.setRowCount(0)
        self.tw_staff.horizontalHeader().setVisible(True)
        self.tw_staff.verticalHeader().setVisible(True)
        self.verticalLayout_2.addWidget(self.tw_staff)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.tw_routes = QtWidgets.QTableWidget(Form)
        self.tw_routes.setObjectName("tw_routes")
        self.tw_routes.setColumnCount(0)
        self.tw_routes.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tw_routes)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(3, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pb_create_person = QtWidgets.QPushButton(Form)
        self.pb_create_person.setObjectName("pb_create_person")
        self.verticalLayout_3.addWidget(self.pb_create_person)
        self.pb_update_person = QtWidgets.QPushButton(Form)
        self.pb_update_person.setObjectName("pb_update_person")
        self.verticalLayout_3.addWidget(self.pb_update_person)
        self.pb_delete_person = QtWidgets.QPushButton(Form)
        self.pb_delete_person.setObjectName("pb_delete_person")
        self.verticalLayout_3.addWidget(self.pb_delete_person)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.le_person_name = QtWidgets.QLineEdit(Form)
        self.le_person_name.setObjectName("le_person_name")
        self.verticalLayout_3.addWidget(self.le_person_name)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.le_person_surname = QtWidgets.QLineEdit(Form)
        self.le_person_surname.setObjectName("le_person_surname")
        self.verticalLayout_3.addWidget(self.le_person_surname)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.le_person_patronymic = QtWidgets.QLineEdit(Form)
        self.le_person_patronymic.setObjectName("le_person_patronymic")
        self.verticalLayout_3.addWidget(self.le_person_patronymic)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.le_person_phone = QtWidgets.QLineEdit(Form)
        self.le_person_phone.setObjectName("le_person_phone")
        self.verticalLayout_3.addWidget(self.le_person_phone)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.te_info = QtWidgets.QTextEdit(Form)
        self.te_info.setObjectName("te_info")
        self.verticalLayout_3.addWidget(self.te_info)
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
        self.label_6.setText(_translate("Form", "Список персонала"))
        self.label_7.setText(_translate("Form", "Список маршрутов"))
        self.pb_create_person.setText(_translate("Form", "Создать"))
        self.pb_update_person.setText(_translate("Form", "Обновить"))
        self.pb_delete_person.setText(_translate("Form", "Удалить"))
        self.label.setText(_translate("Form", "Имя"))
        self.label_2.setText(_translate("Form", "Фамилия"))
        self.label_3.setText(_translate("Form", "Отчество"))
        self.label_4.setText(_translate("Form", "Телефон"))
        self.label_5.setText(_translate("Form", "Инфо"))
