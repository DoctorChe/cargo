from collections import OrderedDict

from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from cargo.ui.views.ui_warehouse import Ui_Form
from cargo.utils.widget_utils import table_cleaner, table_append_rows, combobox_cleaner, combobox_append_rows

H_HEADERS_WAREHOUSE = OrderedDict([
    ('id', 'id'),
    ('address', 'Адрес'),
    ('city', 'Город'),
])

H_HEADERS_ROUTES = OrderedDict([
    ('id', 'id'),
    ('from_warehouse_id', 'Начальный пункт'),
    ('to_warehouse_id', 'Конечный пункт'),
])


class WarehouseListView(QWidget):

    signal_create_warehouse = Signal(dict)
    signal_read_warehouse = Signal(dict)
    signal_update_warehouse = Signal(dict)
    signal_delete_warehouse = Signal(dict)

    signal_get_city_id_by_name = Signal(dict)
    signal_get_city_name_by_id = Signal(dict)
    signal_get_all_cities = Signal()

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.warehouse_id = None
        self.city_id = None

        self.ui.tw_warehouse.setColumnCount(len(H_HEADERS_WAREHOUSE))
        self.ui.tw_warehouse.setHorizontalHeaderLabels(H_HEADERS_WAREHOUSE.values())
        self.ui.tw_warehouse.horizontalHeader().setVisible(True)
        self.ui.tw_warehouse.verticalHeader().setVisible(True)
        self.ui.tw_warehouse.setAlternatingRowColors(True)
        self.ui.tw_warehouse.setColumnHidden(0, True)
        self.ui.tw_warehouse.resizeColumnsToContents()
        self.ui.tw_warehouse.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tw_warehouse.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tw_warehouse.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

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

        self.ui.tw_warehouse.clicked.connect(self.warehouse_table_clicked)
        self.ui.pb_create_warehouse.clicked.connect(self.create_warehouse_clicked)
        self.ui.pb_update_warehouse.clicked.connect(self.update_warehouse_clicked)
        self.ui.pb_delete_warehouse.clicked.connect(self.delete_warehouse_clicked)
        # self.ui.cb_city.currentTextChanged[str].connect(self.signal_get_city_id_by_name)

        self.parent().currentChanged.connect(self.get_all_cities)

    def warehouse_table_clicked(self, idx):
        self.warehouse_id = self.ui.tw_warehouse.item(idx.row(), 0).text()
        self.read_warehouse_clicked()

    def create_warehouse_clicked(self):
        self.signal_create_warehouse.emit(self.get_warehouse_data())

    def read_warehouse_clicked(self):
        if self.warehouse_id:
            warehouse = {'warehouse': {
                'id': self.warehouse_id
            }}
            self.signal_read_warehouse.emit(warehouse)

    def update_warehouse_clicked(self):
        warehouse = self.get_warehouse_data()
        warehouse['warehouse']['id'] = self.warehouse_id
        self.signal_update_warehouse.emit(warehouse)

    def delete_warehouse_clicked(self):
        if self.warehouse_id:
            warehouse = {'warehouse': {
                'id': self.warehouse_id
            }}
            self.signal_delete_warehouse.emit(warehouse)

    def populate_warehouse_table(self, items):
        table_cleaner(self.ui.tw_warehouse)
        table_append_rows(self.ui.tw_warehouse, items, H_HEADERS_WAREHOUSE)

    def populate_routes_table(self, items):
        table_cleaner(self.ui.tw_routes)
        table_append_rows(self.ui.tw_routes, items, H_HEADERS_ROUTES)

    def populate_warehouse_card(self, item):
        self.ui.le_address.setText(item.get('address'))
        self.ui.cb_city.setCurrentText(item.get('city'))

    def get_warehouse_data(self):
        address = self.ui.le_address.text()
        if self.ui.cb_city.currentText():
            self.get_city_id_by_name(self.ui.cb_city.currentText())
            if self.city_id is not None:
                warehouse = {'warehouse': {
                    'address': address,
                    'city_id': self.city_id,
                }}
                return warehouse

    def get_city_id_by_name(self, city_name):
        city = {'city': {
            'name': city_name
        }}
        self.signal_get_city_id_by_name.emit(city)

    def get_city_name_by_id(self, city_id):
        city = {'city': {
            'id': city_id
        }}
        self.signal_get_city_name_by_id.emit(city)

    def populate_cities_combobox(self, items):
        combobox_cleaner(self.ui.cb_city)
        combobox_append_rows(self.ui.cb_city, items)

    def get_all_cities(self):
        self.signal_get_all_cities.emit()
