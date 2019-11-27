from PyQt5 import QtWidgets

from cargo.ui.views.staff_list_view import StaffListView


class RightPanelView(QtWidgets.QTabWidget):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)

        self.tab_staff = StaffListView(parent=self)
        self.addTab(self.tab_staff, 'Staff')
