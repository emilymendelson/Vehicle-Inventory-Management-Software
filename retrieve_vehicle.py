# Module: retrieve_vehicle
# This module enables the user to retrieve specific vehicle information within the data structure based on user input.

# The filereader and menu modules are used.
import filereader
import menu


# The retrieve_vehicle() function allows the user to input a vehicle ID
# The user is able to retrieve the corresponding odometer reading, vehicle availability, or vehicle make.
def retrieve_vehicle():
    print("Welcome to the retrieve vehicle information menu!")
    retrieveVehicleInput = input("Press 1 to retrieve information for a vehicle. "
                                 "Press 2 to return to the main menu.")

    if retrieveVehicleInput == "1":

        vehicleID = input('Enter vehicle ID to retrieve vehicle information:')

        # The prepare_vehicle_info() function is called from filereader module.
        vehicle_info = filereader.prepare_vehicle_info()

        for i in range(len(vehicle_info)):
            if vehicleID == vehicle_info[i][0]:   # If vehicle ID is equal to a vehicle ID in the list.
                choose_variable = input("Press 1 to Retrieve Odometer Reading. "
                                        "Press 2 to Retrieve Vehicle Availability. "
                                        "Press 3 to Retrieve Vehicle Make.")
                if choose_variable == "1":
                    # Print the odometer reading found in the list containing the vehicleID inputted by the user.
                    print('The odometer reading for this vehicle is: ' + str(vehicle_info[i][3]))
                    retrieve_vehicle()
                    break
                if choose_variable == "2":
                    # Print the availability status found in the list containing the vehicleID inputted by the user.
                    print('The availability of this vehicle is: ' + str(vehicle_info[i][6]))
                    retrieve_vehicle()
                    break
                if choose_variable == "3":
                    # Print the make of the vehicle found in the list containing the vehicleID inputted by the user.
                    print('The make of this vehicle is: ' + str(vehicle_info[i][2]))
                    retrieve_vehicle()
                    break
        else:
            print('This vehicle ID does not exist in the database. Please try again.')
            retrieve_vehicle()


    if retrieveVehicleInput == "2":
        menu.menu()


if __name__ =='__main__':
    retrieve_vehicle()
