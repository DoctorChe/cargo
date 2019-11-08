import os

from cargo.app import Cargo
from cargo.utils.parser import create_parser
from cargo.utils.handlers import handle
from cargo.utils.db import Base
from cargo.utils.config import INSTALLED_MODULES, BASE_DIR


parser = create_parser()

if parser.parse_args().migrate:
    module_name_list = [f"cargo.{item}.models" for item in INSTALLED_MODULES]
    module_path_list = (os.path.join(BASE_DIR, item, "models.py") for item in INSTALLED_MODULES)
    for index, path in enumerate(module_path_list):
        if os.path.exists(path):
            __import__(module_name_list[index])
    Base.metadata.create_all()

else:
    with Cargo(handle) as cargo:
        cargo.run()
