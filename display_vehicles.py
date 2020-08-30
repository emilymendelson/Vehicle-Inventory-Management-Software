# Module: display_vehicles

"""The display_vehicles module lists all vehicles, lists vehicles by make, type, and availability, lists vehicle ID
by make, and displays a list based on vehicles matched to words in a keyword search. It can display the vehicle
listings in the console, or it can write the output to a separate text file."""

# The filereader and menu modules are used.
import filereader
import menu


"""The printOrWrite() function allows the user to choose to print output to the console or to write the output to 
a user-named text file."""


def printOrWrite(printStatement, listInfo):
    choosePrintWrite = input ('Press 1 to Print Output. '
                              'Press 2 to Save Output to a Text File.')
    if choosePrintWrite == "1":
        print(printStatement)
    if choosePrintWrite == "2":
        filename = input("Enter a filename: ").lower()
        with open(filename + ".txt", 'w') as filehandle:
            # Each element in the listInfo list is written to the user named text file.
            for listItem in listInfo:
                filehandle.write('%s\n' % listItem)
        print("The file " + filename + ".txt has been created.")


"""The displayVehicleByAttribute function prints or writes to a new file a list of all vehicles, all vehicles of a 
certain make, type, or availability depending on user input."""


def displayVehicleByAttribute(vehicleInput, index):
    # The prepare_vehicle_info() function is called from filereader module.
    vehicle_info = filereader.prepare_vehicle_info()

    outputList = []
    for i in range(len(vehicle_info)):
        # If the vehicleInput is equal to a element within the list of lists, it is added to the new outputList.
        if str(vehicleInput) == str(vehicle_info[i][index]):
            outputList.append(vehicle_info[i])
    if outputList != []:
        printStatement = outputList
        listInfo = outputList
        # The user can choose to print the outputList or write it to a text file.
        printOrWrite(printStatement, listInfo)
    else:
        print("No vehicles were found in the database. Please Try Again.")
        display_vehicles()


"""The display_vehicles() function uses both the printOrWrite function and the displayVehicleByAttribute function.
Users are given a choice of what they choose to display, and then can choose to print the information or write
it to a text file."""


def display_vehicles():

    print("Welcome to the display vehicle menu!")
    displayVehicleInput = input("Press 1 to display vehicle information. "
                                "Press 2 to return to the main menu.")

    if displayVehicleInput == "1":

        display_choice = input('Press 1 to display all vehicles. '
                               'Press 2 to display list all vehicles of a chosen make, type, or availability. '
                               'Press 3 to display all vehicles IDs for a chosen make. '
                               'Press 4 to display all vehicles matching a keyword search. ')

        # The prepare_vehicle_info() function is called from filereader module.
        vehicle_info = filereader.prepare_vehicle_info()

        if display_choice == "1":
            printStatement = vehicle_info
            listInfo = vehicle_info
            # The printOrWrite function is used to allow the user to print or write the list of all vehicle information.
            printOrWrite(printStatement, listInfo)
            display_vehicles()

        if display_choice == "2":
            list_choice = input('Press 1 to display a list of vehicles by make. '
                                'Press 2 to display a list of vehicles by type. '
                                'Press 3 to display a list of vehicles by availability.')

            if list_choice == "1":
                vehicleInput = input("Please Enter the Vehicle Make: ").lower()
                index = 1
                # The displayVehicleByAttribute function prints or writes to a file a list of all vehicles of given make
                displayVehicleByAttribute(vehicleInput, index)
                display_vehicles()

            if list_choice == "2":
                vehicleInput = input("Please Enter the Vehicle Type: ").lower()
                index = 2
                # The displayVehicleByAttribute function prints or writes to a file a list of all vehicles of given type
                displayVehicleByAttribute(vehicleInput, index)
                display_vehicles()

            if list_choice == "3":
                vehicleInput = input("Please Enter the Vehicle Availability: ").lower()
                index = 6
            # The displayVehicleByAttribute function prints/writes to a file a list of all vehicles of given avalability
                displayVehicleByAttribute(vehicleInput, index)
                display_vehicles()

        if display_choice == "3":
            vehicleMake = input("Please Enter the Vehicle Make: ").lower()
            vehicleMakeID = []
            for i in range(len(vehicle_info)):
                if str(vehicleMake) == str(vehicle_info[i][1]):
                    vehicleMakeID.append(vehicle_info[i][0])    # ID of vehicle of inputted make is added to list
            if vehicleMakeID != []:
                printStatement = vehicleMakeID
                listInfo = vehicleMakeID
                # The printOrWrite function is used to allow the user to print/write the list of vehicle IDs
                printOrWrite(printStatement, listInfo)
                display_vehicles()
            else:
                print("No vehicles of this make were found in the database. Please Try Again.")
                display_vehicles()

        if display_choice == "4":
            keywords = input("Enter keywords you want to search for in the database separated by spaces: ").lower()
            # String of words is split into list at spaces
            keywords = keywords.split()
            print(keywords)
            searchResults = []
            for word in keywords:
                for sublist in vehicle_info:
                    # If inputted words are in sublist and the sublist has not already been added to the searchResults
                    if word in sublist and sublist not in searchResults:
                        searchResults.append(sublist)
            print(searchResults)
            display_vehicles()

    if displayVehicleInput == "2":
        menu.menu()


if __name__ =='__main__':
    display_vehicles()
