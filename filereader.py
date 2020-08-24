# Name: Emily Mendelson (20071835)
# Date: Monday, July 20, 2020

# Module: filereader
# This module is used in the add_vehicles, update_vehicles, display_vehicles, and retrieve_vehicles modules.

# The pandas library is imported, and used to read the csv file and create a list of lists from the data.
import pandas as pd


# This function reads the csv file containing the vehicle information and creates a dataframe.
# The dataframe is then converted into a new data structure which is a list of lists, called vehicle_info.
def prepare_vehicle_info():
    # Create a dataframe from csv
    dataframe = pd.read_csv('database1.csv', delimiter=',', skipinitialspace=True)
    dataframe.columns.str.lower()
    # Create a list of lists from dataframe rows
    vehicle_info = [list(row) for row in dataframe.values]
    vehicle_info.insert(0, dataframe.columns.to_list())
    for sublist in vehicle_info:
        for i in range(len(sublist)):
            sublist[i] = str(sublist[i])
            if isinstance(sublist[i], str) == True:
                sublist[i] = sublist[i].lower()
    return vehicle_info


if __name__ =='__main__':
    print(prepare_vehicle_info())
