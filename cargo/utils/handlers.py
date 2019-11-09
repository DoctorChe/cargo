from cargo.utils.config import SERVER_ERROR, NOT_FOUND, WRONG_REQUEST
from cargo.utils.protocol import common_check_command, create_response
from .resolvers import resolve
from .config_log import logger


def handler(command):
    logger.debug(f"Checking command : {command}")
    if common_check_command(command):
        logger.debug(f"Command '{command}' was checked")
        action_name = command.get('action')
        controller = resolve(action_name)
        if controller:
            try:
                logger.debug(f'Controller {action_name} resolved with request: {command}')
                response = controller(command)
            except Exception as e:
                logger.critical(f'Controller {action_name} error: {e}')
                response = create_response(command, SERVER_ERROR, {'message': 'Internal cargo error'})
        else:
            logger.error(f'Controller {action_name} not found')
            response = create_response(command, NOT_FOUND, {'message': f'Action with name {action_name} not supported'})
    else:
        logger.error(f'Command is incorrect: {command}')
        response = create_response(command, WRONG_REQUEST, {'message': 'Command is incorrect'})
    return response
