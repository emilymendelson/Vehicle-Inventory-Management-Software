"""This program reads a data file containing a list of cars and their information including status, odometer
reading and vehicle ID. This data file is then converted into a list of lists. New vehicles can be added through the
add_vehicles module. Vehicle info can be update using through the update_vehicles module. Lists of certain vehicles
can be specified by the user and displayed, or written to a text file. Information for a specific vehicle can
be retrieved through the retrieve_vehicle module."""

# Module: main

# Running the main module starts the program by calling the menu function from the menu module.
# Users can then input a number to choose what they want to do next.

import menu

def main():
    menu.menu()

if __name__ =='__main__':
    menu.menu()
