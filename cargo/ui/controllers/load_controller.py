from PyQt5 import QtCore

from cargo.utils.protocol import create_command


class LoadController(QtCore.QObject):
    def __init__(self, view, handler):
        QtCore.QObject.__init__(self)
        self.view = view
        self._handler = handler

        self.read_all_loads()

        self.view.signal_create_load.connect(self.create_load)
        self.view.signal_read_load.connect(self.read_load)
        self.view.signal_update_load.connect(self.update_load)
        self.view.signal_delete_load.connect(self.delete_load)

    def create_load(self, data):
        action = 'create_load'
        self._handler(create_command(action, data))

        self.read_all_loads()

    def read_all_loads(self, data=None):
        action = 'read_all_loads'
        response = self._handler(create_command(action, data))

        loads = response.get('data').get('loads')
        self.view.populate_load_table(loads)

    def read_load(self, data):
        action = 'read_load'
        response = self._handler(create_command(action, data))

        load = response.get('data').get('load')
        self.view.populate_load_card(load)

    def update_load(self, data):
        action = 'update_load'
        self._handler(create_command(action, data))

        self.read_all_loads()

    def delete_load(self, data):
        action = 'delete_load'
        self._handler(create_command(action, data))

        self.read_all_loads()
