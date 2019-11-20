import codecs
# import pydot
import sadisplay

from cargo.route import models


def generate_schema():
    desc = sadisplay.describe(
        [getattr(models, attr) for attr in dir(models)],
        show_methods=True,
        show_properties=True,
        show_indexes=True,
    )
    with codecs.open('schema.dot', 'w', encoding='utf-8') as f:
        f.write(sadisplay.dot(desc))

    # TODO: Convert dot to png (UnicodeDecodeError now)
    # (graph,) = pydot.graph_from_dot_file('schema.dot')
    # graph.write_png('schema.png')


if __name__ == '__main__':
    generate_schema()
