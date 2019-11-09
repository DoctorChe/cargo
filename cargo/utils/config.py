import os

TEST_MODE = True

if TEST_MODE:
    DATABASE = 'sqlite:///../tests/db.sqlite3'
else:
    DATABASE = 'sqlite:///cargo/db/db.sqlite3'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROGRAM = 'cargo'
VERSION = '0.0.1'

INSTALLED_MODULES = (
    'staff',
    'echo',
)

OK = 200
WRONG_REQUEST = 400
NOT_FOUND = 404
SERVER_ERROR = 500

RESPONSE_CODES = (
    OK,
    WRONG_REQUEST,
    NOT_FOUND,
    SERVER_ERROR,
)
