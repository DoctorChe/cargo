import sys

from PyQt5 import QtCore

from cargo.ui.controllers.city_controller import CityController
from cargo.ui.controllers.load_controller import LoadController
from cargo.ui.controllers.menu_controller import MenuController
from cargo.ui.controllers.route_controller import RouteController
from cargo.ui.controllers.staff_controller import StaffController
from cargo.ui.controllers.vehicle_controller import VehicleController
from cargo.ui.controllers.warehouse_controller import WarehouseController


class MainController(QtCore.QObject):

    def __init__(self, view, handler):
        super(MainController, self).__init__()
        self.view = view
        self._handler = handler
        self._init_controllers()

    def _init_controllers(self):
        self._init_menu_bar()
        self._init_central_panel()

    def exit(self):
        self.view.close()
        sys.exit()

    def _init_menu_bar(self):
        menu = self.view.menuBar()
        self._menu_controller = MenuController(self, menu)

    def _init_central_panel(self):
        self._staff_controller = StaffController(self.view.central_panel.tab_staff, self._handler)
        self._vehicle_controller = VehicleController(self.view.central_panel.tab_vehicle, self._handler)
        self._load_controller = LoadController(self.view.central_panel.tab_load, self._handler)
        self._route_controller = RouteController(self.view.central_panel.tab_route, self._handler)
        self._city_controller = CityController(self.view.central_panel.tab_city, self._handler)
        self._warehouse_controller = WarehouseController(self.view.central_panel.tab_warehouse, self._handler)

    def show(self):
        self.view.show()
