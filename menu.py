# Module: menu

"""This module provides the user with a menu to select options from. The user can choose to add a vehicle, update
or delete a vehicle, display lists of vehicle information, or retrieve information for a vehicle."""

# The add_vehicles, update_vehicles, display_vehicles, and retrieve_vehicle modules are used.
import add_vehicles
import update_vehicles
import display_vehicles
import retrieve_vehicle

# The menu() function allows the user to choose an option leading to another function, depending on the choice.


def menu():
    print("Welcome to the main menu!")
    choose_menu = input('Press 1 to Add a Vehicle. '
                        'Press 2 to Update or Delete a Vehicle. '
                        'Press 3 to Display Lists of Vehicle Information. '
                        'Press 4 to Retrieve Information for a Vehicle. ')
    if choose_menu == "1":
        # The add_vehicle() function is called from the add_vehicles module.
        add_vehicles.add_vehicle()
    if choose_menu == "2":
        # The update_vehicles() function is called from the update_vehicles module.
        update_vehicles.update_vehicles()
    if choose_menu == "3":
        # The display_vehicles() function is called from the display_vehicles module.
        display_vehicles.display_vehicles()
    if choose_menu == "4":
        # The retrieve_vehicle() function is called from the retrieve_vehicle module.
        retrieve_vehicle.retrieve_vehicle()


if __name__ =='__main__':
    menu()
