from PyQt5 import QtCore
from PyQt5 import QtWidgets

from cargo.ui.dialogs.about_dialog import AboutDialog


class MenuController(QtCore.QObject):

    def __init__(self, main_controller, menu):
        super(MenuController, self).__init__()
        self._main_controller = main_controller
        self._menu = menu
        self._init_menu_bar()

    def _init_menu_bar(self):
        self._init_file_menu()
        self._init_help_menu()

    def _init_file_menu(self):
        file_menu = self._menu.addMenu(self.tr('&File'))
        file_menu.addAction(self._create_exit_action())

    def _init_help_menu(self):
        help_menu = self._menu.addMenu(self.tr('&Help'))
        help_menu.addAction(self._create_about_action())
        help_menu.addAction(self._create_aboutqt_action())

    def _create_about_action(self):
        action = QtWidgets.QAction('&About', self)
        action.setShortcuts(["F1"])
        action.triggered.connect(self._about)
        return action

    def _create_aboutqt_action(self):
        action = QtWidgets.QAction('About&Qt', self)
        action.setShortcuts(["F12"])
        action.triggered.connect(self._aboutqt)
        return action

    def _about(self):
        """Show about program window"""
        about_dialog = AboutDialog(self._menu)
        about_dialog.show()

    def _aboutqt(self):
        """Show about Qt window"""
        QtWidgets.QMessageBox.aboutQt(self._menu)

    def _create_exit_action(self):
        # action = QtWidgets.QAction(QtGui.QIcon(self._main_controller.view.style +
        #                                        '/resources/ApplicationExit.png'), self.tr('E&xit'), self)
        action = QtWidgets.QAction(self.tr('E&xit'), self)
        action.setShortcuts(["Ctrl+Q"])
        action.triggered.connect(self._main_controller.exit)
        return action
