from collections import OrderedDict

from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from cargo.ui.views.ui_vehicle import Ui_Form
from cargo.utils.widget_utils import table_cleaner, table_append_rows

H_HEADERS_VEHICLE = OrderedDict([
    ('id', 'id'),
    ('model', 'Модель'),
    ('plate', 'Регистрационный номер'),
    ('year', 'Год выпуска'),
    ('payload', 'Грузоподъёмность'),
    ('run', 'Пробег'),
    ('fuel_consumption', 'Расход топлива'),
    ('volume', 'Объём кузова'),
])

H_HEADERS_ROUTES = OrderedDict([
    ('id', 'id'),
    ('from_warehouse_id', 'Начальный пункт'),
    ('to_warehouse_id', 'Конечный пункт'),
])


class VehicleListView(QWidget):

    signal_create_vehicle = Signal(dict)
    signal_read_vehicle = Signal(dict)
    signal_update_vehicle = Signal(dict)
    signal_delete_vehicle = Signal(dict)

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.vehicle_id = None

        self.ui.tw_vehicle.setColumnCount(len(H_HEADERS_VEHICLE))
        self.ui.tw_vehicle.setHorizontalHeaderLabels(H_HEADERS_VEHICLE.values())
        self.ui.tw_vehicle.horizontalHeader().setVisible(True)
        self.ui.tw_vehicle.verticalHeader().setVisible(True)
        self.ui.tw_vehicle.setAlternatingRowColors(True)
        self.ui.tw_vehicle.setColumnHidden(0, True)
        self.ui.tw_vehicle.resizeColumnsToContents()
        self.ui.tw_vehicle.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tw_vehicle.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tw_vehicle.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

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

        self.ui.tw_vehicle.clicked.connect(self.vehicle_table_clicked)
        self.ui.pb_create_vehicle.clicked.connect(self.create_vehicle_clicked)
        self.ui.pb_update_vehicle.clicked.connect(self.update_vehicle_clicked)
        self.ui.pb_delete_vehicle.clicked.connect(self.delete_vehicle_clicked)

    def vehicle_table_clicked(self, idx):
        self.vehicle_id = self.ui.tw_vehicle.item(idx.row(), 0).text()
        self.read_vehicle_clicked()

    def create_vehicle_clicked(self):
        self.signal_create_vehicle.emit(self.get_vehicle_data())

    def read_vehicle_clicked(self):
        if self.vehicle_id:
            vehicle = {'vehicle': {
                'id': self.vehicle_id
            }}
            self.signal_read_vehicle.emit(vehicle)

    def update_vehicle_clicked(self):
        vehicle = self.get_vehicle_data()
        vehicle['vehicle']['id'] = self.vehicle_id
        self.signal_update_vehicle.emit(vehicle)

    def delete_vehicle_clicked(self):
        if self.vehicle_id:
            vehicle = {'vehicle': {
                'id': self.vehicle_id
            }}
            self.signal_delete_vehicle.emit(vehicle)

    def populate_vehicle_table(self, items):
        table_cleaner(self.ui.tw_vehicle)
        table_append_rows(self.ui.tw_vehicle, items, H_HEADERS_VEHICLE)

    def populate_routes_table(self, items):
        table_cleaner(self.ui.tw_routes)
        table_append_rows(self.ui.tw_routes, items, H_HEADERS_ROUTES)

    def populate_vehicle_card(self, item):
        self.ui.le_model.setText(item.get('model'))
        self.ui.le_plate.setText(item.get('plate'))
        self.ui.sb_year.setValue(item.get('year'))
        self.ui.sb_payload.setValue(item.get('payload'))
        self.ui.sb_run.setValue(item.get('run'))
        self.ui.dsb_fuel_consumption.setValue(item.get('fuel_consumption'))
        self.ui.dsb_volume.setValue(item.get('volume'))

    def get_vehicle_data(self):
        model = self.ui.le_model.text()
        plate = self.ui.le_plate.text()
        year = self.ui.sb_year.value()
        payload = self.ui.sb_payload.value()
        run = self.ui.sb_run.value()
        fuel_consumption = self.ui.dsb_fuel_consumption.value()
        volume = self.ui.dsb_volume.value()
        vehicle = {'vehicle': {
            'model': model,
            'plate': plate,
            'year': year,
            'payload': payload,
            'run': run,
            'fuel_consumption': fuel_consumption,
            'volume': volume,
        }}
        return vehicle
