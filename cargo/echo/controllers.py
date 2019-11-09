from cargo.utils.config import OK

from cargo.utils.decorators import logged
from cargo.utils.protocol import create_response


@logged
def echo_controller(command):
    return create_response(command, OK)
