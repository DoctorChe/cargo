from collections import OrderedDict

from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from cargo.ui.views.ui_route import Ui_Form
from cargo.utils.widget_utils import table_cleaner, table_append_rows

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
        table_cleaner(self.ui.tw_route)
        table_append_rows(self.ui.tw_route, items, H_HEADERS_ROUTE)

    # def populate_routes_table(self, items):
    #     table_cleaner(self.ui.tw_routes)
    #     table_append_rows(self.ui.tw_routes, items, H_HEADERS_ROUTES)

    def populate_route_card(self, item):
        self.ui.le_from_warehouse.setText(item.get('from_warehouse'))
        self.ui.le_to_warehouse.setText(item.get('to_warehouse'))
        self.ui.le_person.setText(item.get('person'))
        self.ui.le_vehicle.setText(item.get('vehicle'))
        self.ui.le_load.setText(item.get('load'))

    def get_route_data(self):
        from_warehouse = self.ui.le_from_warehouse.text()
        to_warehouse = self.ui.le_to_warehouse.text()
        person = self.ui.le_person.text()
        vehicle = self.ui.le_vehicle.text()
        load = self.ui.le_load.text()
        # route = {'route': {
        #     'from_warehouse_id': from_warehouse_id,
        #     'to_warehouse_id': to_warehouse_id,
        #     'person_id': person_id,
        #     'vehicle_id': vehicle_id,
        #     'load_id': load_id,
        # }}
        # return route
