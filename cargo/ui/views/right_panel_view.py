from PyQt5 import QtWidgets

from cargo.ui.views.staff_list_view import StaffListView
from cargo.ui.views.vehicle_list_view import VehicleListView


class RightPanelView(QtWidgets.QTabWidget):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)

        self.tab_staff = StaffListView(parent=self)
        self.addTab(self.tab_staff, 'Staff')
        self.tab_vehicle = VehicleListView(parent=self)
        self.addTab(self.tab_vehicle, 'Vehicle')
