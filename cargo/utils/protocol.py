from datetime import datetime

# from cargo.utils.config import RESPONSE_CODES
from cargo.utils.config_log import logger
from cargo.utils.decorators import logged


@logged
def create_command(action: str, data: dict) -> dict:
    """
    Create command
    :param action: action
    :param data: command's dictionary
    :return: command
    """
    return {
        'action': action,
        'data': data,
        'time': datetime.now().timestamp(),
    }


@logged
# def create_response(request: dict, response_code: int, data=None) -> dict:
def create_response(request: dict, response_str: str, data=None) -> dict:
    """
    Создать сообщение
    :param request: Словарь запроса
    :param response_code: Код ответа
    :param data: Словарь с дополнительными данными в ответе (например описание ошибки)
    :return: Словарь ответа
    """
    # if response_code in RESPONSE_CODES:
    return {
        'action': request.get('action'),
        # 'response': response_code,
        'response': response_str,
        'data': data,
        'time': request.get('time'),
    }


def common_check_command(data: dict) -> bool:
    """
    Common command checking
    :param data: command's dictionary
    :return: checking result
    """

    def check_length(data: dict) -> bool:
        if len(str(data)) <= 640:
            return True
        logger.error("Command length more than 640 symbols")
        return False

    def check_action(data: dict) -> bool:
        if 'action' in data and len(data['action']) <= 25:
            return True
        logger.error(f"Attribute {'action'} is missing or longer than 25 characters")
        return False

    def check_time(data: dict) -> bool:
        if 'time' in data and isinstance(data['time'], float):
            return True
        logger.error(f"Attribute {'time'} is missing or of the wrong type")
        return False

    if check_length(data) and check_action(data) and check_time(data):
        return True

    return False
