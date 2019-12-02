import re
from collections import OrderedDict

from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from cargo.ui.views.ui_route import Ui_Form
from cargo.utils.widget_utils import table_cleaner, table_append_rows, combobox_cleaner, combobox_append_rows

H_HEADERS_ROUTE = OrderedDict([
    ('id', 'id'),
    ('from_warehouse', 'Начальный пункт'),
    ('to_warehouse', 'Конечный пункт'),
    ('person', 'Водитель'),
    ('vehicle', 'Транспортное средство'),
    ('load', 'Груз'),
])

# H_HEADERS_ROUTES = OrderedDict([
#     ('id', 'id'),
#     ('from_warehouse_id', 'Начальный пункт'),
#     ('to_warehouse_id', 'Конечный пункт'),
# ])


class RouteListView(QWidget):

    signal_create_route = Signal(dict)
    signal_read_route = Signal(dict)
    signal_update_route = Signal(dict)
    signal_delete_route = Signal(dict)

    signal_get_from_warehouse_id_by_full_address = Signal(dict)
    signal_get_to_warehouse_id_by_full_address = Signal(dict)
    signal_get_person_id_by_fullname = Signal(dict)
    signal_get_vehicle_id_by_plate = Signal(dict)
    signal_get_load_id_by_info = Signal(dict)

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.route_id = None
        self.from_warehouse_id = None
        self.to_warehouse_id = None
        self.person_id = None
        self.vehicle_id = None
        self.load_id = None

        self.ui.tw_route.setColumnCount(len(H_HEADERS_ROUTE))
        self.ui.tw_route.setHorizontalHeaderLabels(H_HEADERS_ROUTE.values())
        self.ui.tw_route.horizontalHeader().setVisible(True)
        self.ui.tw_route.verticalHeader().setVisible(True)
        self.ui.tw_route.setAlternatingRowColors(True)
        # self.ui.tw_route.setColumnHidden(0, True)
        self.ui.tw_route.resizeColumnsToContents()
        self.ui.tw_route.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tw_route.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tw_route.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

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

        self.ui.tw_route.clicked.connect(self.route_table_clicked)
        self.ui.pb_create_route.clicked.connect(self.create_route_clicked)
        self.ui.pb_update_route.clicked.connect(self.update_route_clicked)
        self.ui.pb_delete_route.clicked.connect(self.delete_route_clicked)

    def route_table_clicked(self, idx):
        self.route_id = self.ui.tw_route.item(idx.row(), 0).text()
        self.read_route_clicked()

    def create_route_clicked(self):
        self.signal_create_route.emit(self.get_route_data())

    def read_route_clicked(self):
        if self.route_id:
            route = {'route': {
                'id': self.route_id
            }}
            self.signal_read_route.emit(route)

    def update_route_clicked(self):
        route = self.get_route_data()
        route['route']['id'] = self.route_id
        self.signal_update_route.emit(route)

    def delete_route_clicked(self):
        if self.route_id:
            route = {'route': {
                'id': self.route_id
            }}
            self.signal_delete_route.emit(route)

    def populate_route_table(self, items):
        # print(items)
        table_cleaner(self.ui.tw_route)
        table_append_rows(self.ui.tw_route, items, H_HEADERS_ROUTE)

    # def populate_routes_table(self, items):
    #     table_cleaner(self.ui.tw_routes)
    #     table_append_rows(self.ui.tw_routes, items, H_HEADERS_ROUTES)

    def populate_route_card(self, item):
        self.ui.cb_from_warehouse.setCurrentText(item.get('from_warehouse'))
        self.ui.cb_to_warehouse.setCurrentText(item.get('to_warehouse'))
        self.ui.cb_person.setCurrentText(item.get('person'))
        self.ui.cb_vehicle.setCurrentText(item.get('vehicle'))
        self.ui.cb_load.setCurrentText(item.get('load'))

    def get_route_data(self):
        route = {'route': {}}

        if self.ui.cb_from_warehouse.currentText():
            self.get_from_warehouse_id_by_full_address(self.ui.cb_from_warehouse.currentText())
            if self.from_warehouse_id is not None:
                route['route']['from_warehouse_id'] = self.from_warehouse_id

        if self.ui.cb_to_warehouse.currentText():
            self.get_to_warehouse_id_by_full_address(self.ui.cb_to_warehouse.currentText())
            if self.to_warehouse_id is not None:
                route['route']['to_warehouse_id'] = self.to_warehouse_id

        if self.ui.cb_person.currentText():
            self.get_person_id_by_fullname(self.ui.cb_person.currentText())
            if self.person_id is not None:
                route['route']['person_id'] = self.person_id

        if self.ui.cb_vehicle.currentText():
            self.get_vehicle_id_by_plate(self.ui.cb_vehicle.currentText())
            if self.vehicle_id is not None:
                route['route']['vehicle_id'] = self.vehicle_id

        if self.ui.cb_load.currentText():
            self.get_load_id_by_info(self.ui.cb_load.currentText())  # TODO: change info to person
            if self.load_id is not None:
                route['route']['load_id'] = self.load_id
        return route

    def get_from_warehouse_id_by_full_address(self, full_address):
        result = re.findall(r'(.+) \((.+)\)', full_address)
        warehouse = {'warehouse': {
            # 'full_address': full_address,
            'address': result[0][0],
            'city_name': result[0][1],
        }}
        self.signal_get_from_warehouse_id_by_full_address.emit(warehouse)

    def get_to_warehouse_id_by_full_address(self, full_address):
        result = re.findall(r'(.+) \((.+)\)', full_address)
        warehouse = {'warehouse': {
            # 'full_address': full_address,
            'address': result[0][0],
            'city_name': result[0][1],
        }}
        self.signal_get_to_warehouse_id_by_full_address.emit(warehouse)

    def get_person_id_by_fullname(self, fullname):
        fullname_list = fullname.split(' ')
        name, surname = fullname_list[0], fullname_list[1]
        patronymic = ''
        if len(fullname_list) > 2:
            patronymic = fullname_list[2]

        person = {'person': {
            'name': name,
            'surname': surname,
            'patronymic': patronymic or '',
        }}
        self.signal_get_person_id_by_fullname.emit(person)

    def get_vehicle_id_by_plate(self, plate):
        vehicle = {'vehicle': {
            'plate': plate,
        }}
        self.signal_get_vehicle_id_by_plate.emit(vehicle)

    def get_load_id_by_info(self, info):
        load = {'load': {
            'info': info,
        }}
        self.signal_get_load_id_by_info.emit(load)

    def populate_from_warehouse_combobox(self, items):
        combobox_cleaner(self.ui.cb_from_warehouse)
        combobox_append_rows(self.ui.cb_from_warehouse, items)

    def populate_to_warehouse_combobox(self, items):
        combobox_cleaner(self.ui.cb_to_warehouse)
        combobox_append_rows(self.ui.cb_to_warehouse, items)

    def populate_persons_combobox(self, items):
        combobox_cleaner(self.ui.cb_person)
        combobox_append_rows(self.ui.cb_person, items)

    def populate_vehicles_combobox(self, items):
        combobox_cleaner(self.ui.cb_vehicle)
        combobox_append_rows(self.ui.cb_vehicle, items)

    def populate_loads_combobox(self, items):
        combobox_cleaner(self.ui.cb_load)
        combobox_append_rows(self.ui.cb_load, items)

    # def get_all_cities(self):
    #     self.signal_get_all_cities.emit()
