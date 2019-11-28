from collections import OrderedDict

from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from cargo.ui.views.ui_city import Ui_Form
from cargo.utils.table_utils import table_cleaner, table_append_rows

H_HEADERS_CITY = OrderedDict([
    ('id', 'id'),
    ('name', 'Наименоване'),
])

H_HEADERS_WAREHOUSES = OrderedDict([
    ('id', 'id'),
    ('address', 'Адрес'),
    ('city', 'Город'),
])

# H_HEADERS_ROUTES = OrderedDict([
#     ('id', 'id'),
#     ('from_warehouse_id', 'Начальный пункт'),
#     ('to_warehouse_id', 'Конечный пункт'),
# ])


class CityListView(QWidget):

    signal_create_city = Signal(dict)
    signal_read_city = Signal(dict)
    signal_update_city = Signal(dict)
    signal_delete_city = Signal(dict)

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.city_id = None

        self.ui.tw_city.setColumnCount(len(H_HEADERS_CITY))
        self.ui.tw_city.setHorizontalHeaderLabels(H_HEADERS_CITY.values())
        self.ui.tw_city.horizontalHeader().setVisible(True)
        self.ui.tw_city.verticalHeader().setVisible(True)
        self.ui.tw_city.setAlternatingRowColors(True)
        self.ui.tw_city.setColumnHidden(0, True)
        self.ui.tw_city.resizeColumnsToContents()
        self.ui.tw_city.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tw_city.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tw_city.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.ui.tw_warehouses.setColumnCount(len(H_HEADERS_CITY))
        self.ui.tw_warehouses.setHorizontalHeaderLabels(H_HEADERS_CITY.values())
        self.ui.tw_warehouses.horizontalHeader().setVisible(True)
        self.ui.tw_warehouses.verticalHeader().setVisible(True)
        self.ui.tw_warehouses.setAlternatingRowColors(True)
        self.ui.tw_warehouses.setColumnHidden(0, True)
        self.ui.tw_warehouses.resizeColumnsToContents()
        self.ui.tw_warehouses.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tw_warehouses.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tw_warehouses.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        # self.ui.tw_routes.setColumnCount(len(H_HEADERS_ROUTES))
        # self.ui.tw_routes.setHorizontalHeaderLabels(H_HEADERS_ROUTES.values())
        # self.ui.tw_routes.horizontalHeader().setVisible(True)
        # self.ui.tw_routes.verticalHeader().setVisible(True)
        # self.ui.tw_routes.setAlternatingRowColors(True)
        # self.ui.tw_routes.setColumnHidden(0, True)
        # self.ui.tw_routes.resizeColumnsToContents()
        # self.ui.tw_routes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.ui.tw_routes.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.ui.tw_routes.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.ui.tw_city.clicked.connect(self.city_table_clicked)
        self.ui.pb_create_city.clicked.connect(self.create_city_clicked)
        self.ui.pb_update_city.clicked.connect(self.update_city_clicked)
        self.ui.pb_delete_city.clicked.connect(self.delete_city_clicked)

    def city_table_clicked(self, idx):
        self.city_id = self.ui.tw_city.item(idx.row(), 0).text()
        self.read_city_clicked()

    def create_city_clicked(self):
        self.signal_create_city.emit(self.get_city_data())

    def read_city_clicked(self):
        if self.city_id:
            city = {'city': {
                'id': self.city_id
            }}
            self.signal_read_city.emit(city)

    def update_city_clicked(self):
        city = self.get_city_data()
        city['city']['id'] = self.city_id
        self.signal_update_city.emit(city)

    def delete_city_clicked(self):
        if self.city_id:
            city = {'city': {
                'id': self.city_id
            }}
            self.signal_delete_city.emit(city)

    def populate_city_table(self, items):
        table_cleaner(self.ui.tw_city)
        table_append_rows(self.ui.tw_city, items, H_HEADERS_CITY)

    def populate_warehouses_table(self, items):
        table_cleaner(self.ui.tw_warehouses)
        table_append_rows(self.ui.tw_warehouses, items, H_HEADERS_WAREHOUSES)

    # def populate_routes_table(self, items):
    #     table_cleaner(self.ui.tw_routes)
    #     table_append_rows(self.ui.tw_routes, items, H_HEADERS_ROUTES)

    def populate_city_card(self, item):
        self.ui.le_name.setText(item.get('name'))

    def get_city_data(self):
        name = self.ui.le_name.text()
        city = {'city': {
            'name': name,
        }}
        return city
