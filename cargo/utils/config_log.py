import logging.handlers

from contextlib import suppress
from pathlib import Path

from cargo.utils.config import PROGRAM

LOG_FOLDER_PATH = Path.home() / f".{PROGRAM}" / "logs"

with suppress(FileExistsError):
    LOG_FOLDER_PATH.mkdir(mode=0o777, parents=True, exist_ok=True)

# Путь до серверного лога
SERVER_LOG_FILE_PATH = LOG_FOLDER_PATH / "server.log"

# Создаём именованный объект-логгер с именем server
logger = logging.getLogger("server")

# Создаём обработчик с ротацией файлов по дням
server_handler = logging.handlers.TimedRotatingFileHandler(SERVER_LOG_FILE_PATH, when="d", encoding="utf-8")

# Создаём объект форматирования
formatter = logging.Formatter("%(asctime)-10s %(levelname)s %(module)s %(message)s")

# Cвязываем обработчик с форматтером
server_handler.setFormatter(formatter)

server_handler_stream = logging.StreamHandler()
server_handler_stream.setFormatter(formatter)

# Связываем логгер с обработчиком
if not logger.__dict__["handlers"]:
    logger.addHandler(server_handler)
    logger.addHandler(server_handler_stream)

# Устанавливаем уровень сообщений логгера
# server_logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)


# отладка
if __name__ == '__main__':
    logger.critical('Test critical event')
    logger.error('Test error event')
    logger.debug('Test debug event')
    logger.info('Test info event')
