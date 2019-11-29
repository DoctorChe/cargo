from PyQt5 import QtWidgets

from cargo.ui.views.city_list_view import CityListView
from cargo.ui.views.load_list_view import LoadListView
from cargo.ui.views.route_list_view import RouteListView
from cargo.ui.views.staff_list_view import StaffListView
from cargo.ui.views.vehicle_list_view import VehicleListView
from cargo.ui.views.warehouse_list_view import WarehouseListView


class RightPanelView(QtWidgets.QTabWidget):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)

        self.tab_staff = StaffListView(parent=self)
        self.addTab(self.tab_staff, 'Staff')
        self.tab_vehicle = VehicleListView(parent=self)
        self.addTab(self.tab_vehicle, 'Vehicle')
        self.tab_load = LoadListView(parent=self)
        self.addTab(self.tab_load, 'Load')
        self.tab_route = RouteListView(parent=self)
        self.addTab(self.tab_route, 'Route')
        self.tab_warehouse = WarehouseListView(parent=self)
        self.addTab(self.tab_warehouse, 'Warehouse')
        self.tab_city = CityListView(parent=self)
        self.addTab(self.tab_city, 'City')
