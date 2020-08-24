# Name: Emily Mendelson (20071835)
# Date: Monday, July 20, 2020

# Module: add_vehicles
# This module enables the user to add a new vehicle to the data structure, vehicle_info.

# The filereader and menu modules are used.
import filereader
import menu

# The add_vehicle function enables the user to add a new vehicle to the data structure through user input.
def add_vehicle():
    new_vehicle = []

    print("Welcome to the add vehicle menu!")
    addVehicleInput = input("Press 1 to add vehicle. "
                            "Press 2 to return to the main menu.")

    if addVehicleInput == "1":

        vehicleID = input("Please Enter the Vehicle ID:")
        # While the vehicle ID input is not numerical, the user will be prompted to try again.
        while vehicleID.isdigit() != True:
            vehicleID = input("The vehicle ID you entered was not an integer. Please try again:")
        new_vehicle.append(vehicleID)   # The vehicleID will be added to the end of the new_vehicle list.

        vehicleMake = input("Please Enter the Vehicle Make:").lower()
        new_vehicle.append(vehicleMake)

        vehicleType = input("Please Enter the Vehicle Type:").lower()
        new_vehicle.append(vehicleType)

        vehicleOdometer = input("Please Enter the Odometer Reading:")
        # While the vehicleOdometer input is not numerical, the user will be prompted to try again.
        while vehicleOdometer.isdigit() != True:
            vehicleOdometer = input("The odometer reading you entered was not an integer. Please try again:")
        new_vehicle.append(vehicleOdometer)

        vehicleCost = input("Please Enter the Cost to Rent Per Day:")
        # While the vehicleCost input is not numerical, the user will be prompted to try again.
        while vehicleCost.isdigit() != True:
            vehicleCost = input("The cost to rent per day you entered was not an integer. Please try again:")
        new_vehicle.append(vehicleCost)

        vehicleRentals = input("Please Enter the Number of Times the Vehicle Has Been Rented:")
        # While the vehicleRentals input is not numerical, the user will be prompted to try again.
        while vehicleRentals.isdigit() != True:
            vehicleRentals = input("The value you entered for the number of times the vehicle has "
                                   "been rented is not an integer. Please try again:")
        new_vehicle.append(vehicleRentals)

        vehicleStatus = "available"
        new_vehicle.append(vehicleStatus)

        # The prepare_vehicle_info() function is called from filereader module.
        vehicle_info = filereader.prepare_vehicle_info()

        # The new_vehicle list created from user input, is added to the vehicle_info list.
        vehicle_info.append(new_vehicle)

        print('The new vehicle has been successfully added to the data structure: ')
        print(vehicle_info)
        menu.menu() # After the vehicle has been successfully added, the user returns to the menu function.

    if addVehicleInput == "2":
        menu.menu()

if __name__ =='__main__':
    add_vehicle()
