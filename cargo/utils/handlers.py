from cargo.utils.protocol import common_check_command
from .resolvers import resolve
from .config_log import logger


def handle(command):
    logger.debug(f"Checking command : {command}")
    if common_check_command(command):
        logger.debug(f"Command '{command}' was checked")
        action_name = command.get('action')
        controller = resolve(action_name)
        if controller:
            try:
                logger.debug(f'Controller {action_name} resolved with request: {command}')
                # response = controller(command.get('data'))
                response = controller(command)
            except Exception as e:
                logger.critical(f'Controller {action_name} error: {e}')
                response = 'Internal cargo error'
        else:
            logger.error(f'Controller {action_name} not found')
            response = f'Action with name {action_name} not supported'
    else:
        logger.error(f'Command is incorrect: {command}')
        response = f'Command is incorrect'
    return response

    # response = create_response(command, WRONG_REQUEST, {MESSAGE: "Запрос некорректен."})
