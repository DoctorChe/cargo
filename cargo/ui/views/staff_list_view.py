from collections import OrderedDict

from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from cargo.ui.views.ui_staff import Ui_Form
from cargo.utils.table_utils import table_cleaner, table_append_rows

H_HEADERS_STAFF = OrderedDict([
    ('id', 'id'),
    ('name', 'Имя'),
    ('surname', 'Фамилия'),
    ('patronymic', 'Отчество'),
    ('phone', 'Телефон'),
])

H_HEADERS_ROUTES = OrderedDict([
    ('id', 'id'),
    ('from_warehouse_id', 'Начальный пункт'),
    ('to_warehouse_id', 'Конечный пункт'),
])


class StaffListView(QWidget):

    signal_create_person = Signal(dict)
    signal_read_person = Signal(dict)
    signal_update_person = Signal(dict)
    signal_delete_person = Signal(dict)

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.person_id = None

        self.ui.tw_staff.setColumnCount(len(H_HEADERS_STAFF))
        self.ui.tw_staff.setHorizontalHeaderLabels(H_HEADERS_STAFF.values())
        self.ui.tw_staff.horizontalHeader().setVisible(True)
        self.ui.tw_staff.verticalHeader().setVisible(True)
        self.ui.tw_staff.setAlternatingRowColors(True)
        self.ui.tw_staff.setColumnHidden(0, True)
        self.ui.tw_staff.resizeColumnsToContents()
        self.ui.tw_staff.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tw_staff.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tw_staff.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.ui.tw_routes.setColumnCount(len(H_HEADERS_ROUTES))
        self.ui.tw_routes.setHorizontalHeaderLabels(H_HEADERS_ROUTES.values())
        self.ui.tw_routes.horizontalHeader().setVisible(True)
        self.ui.tw_routes.verticalHeader().setVisible(True)
        self.ui.tw_routes.setAlternatingRowColors(True)
        self.ui.tw_routes.setColumnHidden(0, True)
        self.ui.tw_routes.resizeColumnsToContents()
        self.ui.tw_routes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tw_routes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tw_routes.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.ui.tw_staff.clicked.connect(self.staff_table_clicked)
        self.ui.pb_create_person.clicked.connect(self.create_person_clicked)
        self.ui.pb_update_person.clicked.connect(self.update_person_clicked)
        self.ui.pb_delete_person.clicked.connect(self.delete_person_clicked)

    def staff_table_clicked(self, idx):
        self.person_id = self.ui.tw_staff.item(idx.row(), 0).text()
        self.read_person_clicked()

    def create_person_clicked(self):
        self.signal_create_person.emit(self.get_person_data())

    def read_person_clicked(self):
        if self.person_id:
            person = {'person': {
                'id': self.person_id
            }}
            self.signal_read_person.emit(person)

    def update_person_clicked(self):
        person = self.get_person_data()
        person['person']['id'] = self.person_id
        self.signal_update_person.emit(person)

    def delete_person_clicked(self):
        if self.person_id:
            person = {'person': {
                'id': self.person_id
            }}
            self.signal_delete_person.emit(person)

    def populate_staff_table(self, items):
        table_cleaner(self.ui.tw_staff)
        table_append_rows(self.ui.tw_staff, items, H_HEADERS_STAFF)

    def populate_routes_table(self, items):
        table_cleaner(self.ui.tw_routes)
        table_append_rows(self.ui.tw_routes, items, H_HEADERS_ROUTES)

    def populate_staff_card(self, item):
        self.ui.le_person_name.setText(item.get('name'))
        self.ui.le_person_surname.setText(item.get('surname'))
        self.ui.le_person_patronymic.setText(item.get('patronymic'))
        self.ui.le_person_phone.setText(item.get('phone'))
        self.ui.te_info.setText(item.get('info'))

    def get_person_data(self):
        name = self.ui.le_person_name.text()
        surname = self.ui.le_person_surname.text()
        patronymic = self.ui.le_person_patronymic.text()
        phone = self.ui.le_person_phone.text()
        info = self.ui.te_info.toPlainText()
        person = {'person': {
            'name': name,
            'surname': surname,
            'patronymic': patronymic,
            'phone': phone,
            'info': info,
        }}
        print(person)
        return person
