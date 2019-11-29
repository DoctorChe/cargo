import os
import sys

from PyQt5.QtWidgets import QApplication

from cargo.app import Cargo
from cargo.ui.controllers.main_controller import MainController
from cargo.ui.views.main_view import MainView
from cargo.utils.parser import create_parser
from cargo.utils.handlers import handler
from cargo.utils.db import Base
from cargo.utils.config import INSTALLED_MODULES, BASE_DIR
from cargo.utils.schema import generate_schema

parser = create_parser()


def _create_controller(handler):
    window = MainView()
    # dialogs = Dialogs(window, 'CompanyStatistics')
    # return MainController(window, dialogs)
    return MainController(window, handler)


if parser.parse_args().migrate:
    module_name_list = [f'cargo.{item}.models' for item in INSTALLED_MODULES]
    module_path_list = (os.path.join(BASE_DIR, item, 'models.py') for item in INSTALLED_MODULES)
    for index, path in enumerate(module_path_list):
        if os.path.exists(path):
            __import__(module_name_list[index])
    Base.metadata.create_all()

elif parser.parse_args().schema:
    generate_schema()

else:
    app = QApplication(sys.argv)

    with Cargo(handler) as cargo:
        # cargo.run()
        controller = _create_controller(handler)
        controller.show()
        sys.exit(app.exec_())
