import codecs
import os
from pathlib import Path

import pydot
import sadisplay

from cargo.route import models
from .config import BASE_DIR


def generate_schema():
    p_dot = Path(BASE_DIR, 'utils', 'schema.dot')
    p_png = Path(BASE_DIR, 'utils', 'schema.png')

    desc = sadisplay.describe(
        [getattr(models, attr) for attr in dir(models)],
        show_methods=True,
        show_properties=True,
        show_indexes=True,
    )

    with codecs.open(p_dot, 'w', encoding='utf-8') as f:
        f.write(sadisplay.dot(desc))

    with open(p_dot, 'r', encoding='utf-8') as f:
        s = f.read()
    with open(p_dot, 'w', encoding='cp1251') as f:
        f.write(s.encode('cp1251', errors='ignore').decode('cp1251'))

    if os.name == 'nt':
        try:
            from .config_dot_win import DOT_PATH
        except ModuleNotFoundError:
            pass
        else:
            os.environ["PATH"] += os.pathsep + DOT_PATH

    try:
        (graph,) = pydot.graph_from_dot_file(p_dot, encoding='utf-8')
        graph.write_png(p_png)
    except FileNotFoundError as e:
        print(e.args[1])
        if e.args[1] == '"dot" not found in path.':
            print('Probably "dot" not installed')


if __name__ == '__main__':
    generate_schema()
