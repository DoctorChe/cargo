import argparse
from .config import PROGRAM, VERSION


def create_parser():
    """
    Creating a command line parser object
    :return: ArgumentParser object
    """
    parser = argparse.ArgumentParser(
        prog=PROGRAM,
        description='''Cargo tracking application''',
        # epilog='''(c) Doctor_Che 2019. The author of the program, as always, is not responsible for anything.''',
        add_help=False
    )
    parser.add_argument('-h', '--help',
                        action='help',
                        help='Help')
    parser.add_argument('-v', '--version',
                        action='version',
                        help='Show version number',
                        version=f'{PROGRAM} {VERSION}')
    parser.add_argument('-m', '--migrate',
                        action='store_true',
                        help='Migrate')
    parser.add_argument('-s', '--schema',
                        action='store_true',
                        help='Generate database schema (dot format)')
    return parser
