import os

# База данных для хранения данных сервера:
DATABASE = "sqlite:///cargo/db/db.sqlite3"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROGRAM = "cargo"
VERSION = "0.0.1"

INSTALLED_MODULES = (
    "staff",
    # "auth",
    # "contact",
)

OK = 200  # OK
WRONG_REQUEST = 400  # неправильный запрос

RESPONSE_CODES = (
    OK,
    WRONG_REQUEST,
)
