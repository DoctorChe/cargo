from cargo.utils.config_log import logger
from cargo.utils.protocol import create_command


class Cargo:
    def __init__(self, handler):
        self._handler = handler

    def __enter__(self):
        logger.info("Cargo started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        message = 'Cargo shutdown'
        if exc_type:
            if exc_type is not KeyboardInterrupt:
                message = 'Cargo stopped with error'
        logger.info(message)
        return True

    def run(self):
        pass
