from PyQt5 import QtCore

from cargo.utils.protocol import create_command


class RouteController(QtCore.QObject):
    def __init__(self, view, handler):
        QtCore.QObject.__init__(self)
        self.view = view
        self._handler = handler

        self.read_all_routes()

        self.view.signal_create_route.connect(self.create_route)
        self.view.signal_read_route.connect(self.read_route)
        self.view.signal_update_route.connect(self.update_route)
        self.view.signal_delete_route.connect(self.delete_route)

    def create_route(self, data):
        action = 'create_route'
        self._handler(create_command(action, data))

        self.read_all_routes()

    def read_all_routes(self, data=None):
        action = 'read_all_routes'
        response = self._handler(create_command(action, data))

        routes = response.get('data').get('routes')
        self.view.populate_route_table(routes)

    def read_route(self, data):
        action = 'read_route'
        response = self._handler(create_command(action, data))

        route = response.get('data').get('route')
        self.view.populate_route_card(route)

    def update_route(self, data):
        action = 'update_route'
        self._handler(create_command(action, data))

        self.read_all_routes()

    def delete_route(self, data):
        action = 'delete_route'
        self._handler(create_command(action, data))

        self.read_all_routes()
