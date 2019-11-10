from .controllers import (
    create_load_controller,
    read_load_controller,
    read_loads_controller,
    update_load_controller,
    delete_load_controller
)

action_names = [
    {'action': 'create_load', "controller": create_load_controller},
    {'action': 'read_load', "controller": read_load_controller},
    {'action': 'read_all_loads', "controller": read_loads_controller},
    {'action': 'update_load', "controller": update_load_controller},
    {'action': 'delete_load', "controller": delete_load_controller},
]
