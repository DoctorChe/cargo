from .controllers import (
    create_person_controller,
    read_person_controller,
    read_persons_controller,
    update_person_controller,
    delete_person_controller
)

action_names = [
    {'action': 'create_person', "controller": create_person_controller},
    {'action': 'read_person', "controller": read_person_controller},
    {'action': 'read_all_persons', "controller": read_persons_controller},
    {'action': 'update_person', "controller": update_person_controller},
    {'action': 'delete_person', "controller": delete_person_controller},
]
