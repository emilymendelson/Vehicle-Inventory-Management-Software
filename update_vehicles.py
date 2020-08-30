# Module: update_vehicles
# This module enables the user to update or delete vehicle information within the data structure, vehicle_info.

# The filereader and menu modules are used.
import filereader
import menu


# The update_vehicles() function allows the user to update or delete vehicles within the list, vehicle_info.
def update_vehicles():
    print("Welcome to the update vehicle menu!")
    updateVehicleInput = input("Press 1 to update/delete a vehicle. "
                            "Press 2 to return to the main menu.")

    if updateVehicleInput == "1":

        vehicleID = input("Please Enter the Vehicle ID: ")
        # While the vehicle ID input is not numerical, the user will be prompted to try again.
        while vehicleID.isdigit() != True:
            vehicleID = input("The vehicle ID you entered was not numerical. Please try again: ")

        # The prepare_vehicle_info() function is called from filereader module.
        vehicle_info = filereader.prepare_vehicle_info()
        for i in range(len(vehicle_info)):
            if vehicleID == vehicle_info[i][0]:   # If vehicle ID is equal to a vehicle ID in the list, then edit.
                edit_choice = input('Press 1 to edit odometer, press 2 to edit cost, press 3 to change status, '
                                    'or press 4 to delete the vehicle: ')
                if edit_choice == "1":
                    # Edit the odometer reading in the same vehicle_info list as the inputted vehicleID.
                    vehicle_info[i][3] = input('Enter new odometer reading: ')
                    break
                if edit_choice == "2":
                    # Edit the cost in the same vehicle_info list as the inputted vehicleID.
                    vehicle_info[i][4] = input('Enter new cost per hour: ')
                    break
                if edit_choice == "3":
                    # Edit the status in the same vehicle_info list as the inputted vehicleID.
                    vehicle_info[i][6] = input('Enter new status for vehicle: ').lower()
                    break
                if edit_choice == "4":
                    confirm_deletion = input('Press 1 to confirm that you want to delete this vehicle and its information'
                                             'from the database: ')
                    if confirm_deletion == "1":
                        # Delete the video in the same vehicle_info list as the inputted vehicleID.
                        del vehicle_info[i]
                        print('The vehicle was deleted from the database. To update/delete'
                              'a new vehicle enter another vehicle ID.')
                        update_vehicles()
                        break
                    else:
                        print('The vehicle was not deleted from the database.')
                        update_vehicles()
        else:
            print('This vehicle ID does not exist in the database. Please try again.')
            update_vehicles()

    print("Vehicle has been updated successfully.")
    update_vehicles()

    if updateVehicleInput == "2":
        menu.menu()

if __name__ =='__main__':
    update_vehicles()

