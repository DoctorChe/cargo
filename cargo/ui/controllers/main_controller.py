import sys

from PyQt5 import QtCore

from cargo.ui.controllers.menu_controller import MenuController
from cargo.ui.controllers.staff_controller import StaffController


class MainController(QtCore.QObject):

    def __init__(self, view, handler):
        super(MainController, self).__init__()
        self.view = view
        self._handler = handler
        self._init_controllers()

    def _init_controllers(self):
        self._init_menu_bar()
        self._init_right_panel()

    def exit(self):
        self.view.close()
        sys.exit()

    def _init_menu_bar(self):
        menu = self.view.menuBar()
        self._menu_controller = MenuController(self, menu)

    def _init_right_panel(self):
        self._staff_controller = StaffController(self.view.right_panel.tab_staff, self._handler)

    def show(self):
        self.view.show()
