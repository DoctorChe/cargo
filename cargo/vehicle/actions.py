from .controllers import (
    create_vehicle_controller,
    read_vehicle_controller,
    read_vehicle_by_plate_controller,
    read_routes_of_vehicle_controller,
    read_vehicles_controller,
    update_vehicle_controller,
    delete_vehicle_controller
)

action_names = [
    {'action': 'create_vehicle', "controller": create_vehicle_controller},
    {'action': 'read_vehicle', "controller": read_vehicle_controller},
    {'action': 'read_vehicle_by_plate', "controller": read_vehicle_by_plate_controller},
    {'action': 'read_routes_of_vehicle', "controller": read_routes_of_vehicle_controller},
    {'action': 'read_all_vehicles', "controller": read_vehicles_controller},
    {'action': 'update_vehicle', "controller": update_vehicle_controller},
    {'action': 'delete_vehicle', "controller": delete_vehicle_controller},
]
