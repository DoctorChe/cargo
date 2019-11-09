from cargo.utils.config_log import logger
from cargo.utils.protocol import create_command


class Cargo:
    def __init__(self, handler):
        self._handler = handler

    def __enter__(self):
        logger.info("Cargo started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        message = "Cargo shutdown"
        if exc_type:
            if exc_type is not KeyboardInterrupt:
                message = "Cargo stopped with error"
        logger.info(message)
        return True

    def run(self):
        id = 1
        command = create_command('read_all_persons', dict())
        response = self._handler(command)
        logger.info(response)
        command = create_command('create_person', {'person': {'name': 'Duncan', 'surname': 'MacLeod'}})
        response = self._handler(command)
        logger.info(response)
        command = create_command('read_person', {'person': {'id': id}})
        response = self._handler(command)
        logger.info(response)
        command = create_command('update_person', {'person': {'id': id, 'name': 'Scotch'}})
        response = self._handler(command)
        logger.info(response)
        command = create_command('read_person', {'person': {'id': id}})
        response = self._handler(command)
        logger.info(response)
        command = create_command('delete_person', {'person': {'id': id}})
        response = self._handler(command)
        logger.info(response)
        command = create_command('read_person', {'person': {'id': id}})
        response = self._handler(command)
        logger.info(response)
