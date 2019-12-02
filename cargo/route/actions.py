from .controllers import (
    create_city_controller,
    read_city_name_by_id_controller,
    read_city_id_by_name_controller,
    read_cities_controller,
    update_city_controller,
    delete_city_controller,

    create_warehouse_controller,
    read_warehouse_controller,
    read_warehouse_by_full_address_controller,
    read_warehouses_controller,
    read_warehouses_of_city_controller,
    update_warehouse_controller,
    delete_warehouse_controller,

    create_route_controller,
    read_route_controller,
    read_routes_controller,
    update_route_controller,
    delete_route_controller,
)

action_names = [
    {'action': 'create_city', 'controller': create_city_controller},
    {'action': 'read_city', 'controller': read_city_name_by_id_controller},
    {'action': 'read_city_id_by_name', 'controller': read_city_id_by_name_controller},
    {'action': 'read_all_cities', 'controller': read_cities_controller},
    {'action': 'update_city', "controller": update_city_controller},
    {'action': 'delete_city', "controller": delete_city_controller},

    {'action': 'create_warehouse', "controller": create_warehouse_controller},
    {'action': 'read_warehouse', 'controller': read_warehouse_controller},
    {'action': 'read_warehouse_by_full_address', 'controller': read_warehouse_by_full_address_controller},
    {'action': 'read_all_warehouses', 'controller': read_warehouses_controller},
    {'action': 'read_warehouses_of_city', 'controller': read_warehouses_of_city_controller},
    {'action': 'update_warehouse', "controller": update_warehouse_controller},
    {'action': 'delete_warehouse', "controller": delete_warehouse_controller},

    {'action': 'create_route', "controller": create_route_controller},
    {'action': 'read_route', "controller": read_route_controller},
    {'action': 'read_all_routes', "controller": read_routes_controller},
    {'action': 'update_route', "controller": update_route_controller},
    {'action': 'delete_route', "controller": delete_route_controller},
]
