import argparse
from .config import PROGRAM, VERSION


def create_parser():
    """
    Создание объекта парсера командной строки
    :return: объект ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog=PROGRAM,
        description="""Приложение для учета грузоперевозок""",
        # epilog="""(c) Doctor_Che 2019. Автор программы, как всегда, не несет никакой ответственности ни за что.""",
        add_help=False
    )
    parser.add_argument("-h", "--help",
                        action="help",
                        help="Справка")
    parser.add_argument("-v", "--version",
                        action="version",
                        help="Вывести номер версии",
                        version=f"{PROGRAM} {VERSION}")
    parser.add_argument("-m", "--migrate",
                        action="store_true",
                        help="Осуществить миграцию")
    return parser
