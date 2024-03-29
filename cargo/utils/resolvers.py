from functools import reduce
from .config import INSTALLED_MODULES


def get_actions():
    modules = reduce(
        lambda value, item: value + [__import__(f'{item}.actions')],
        INSTALLED_MODULES, []
    )
    submodules = reduce(
        lambda value, item: value + [getattr(item, 'actions', [])],
        modules, []
    )
    action_names = reduce(
        lambda value, item: value + getattr(item, 'action_names', []),
        submodules, []
    )
    return {itm.get('action'): itm.get('controller') for itm in action_names}


def resolve(action_name, actions=None):
    action_names = actions or get_actions()
    return action_names.get(action_name)
