""" CSC108 Assignment 2 Starter code """

from typing import List, TextIO

# A set of constants, each representing a list index for station information.
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
IS_RENTING = 7
IS_RETURNING = 8

####### BEGIN HELPER FUNCTIONS ####################

def is_number(value: str) -> bool:
    """Return True if and only if value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    """

    return value.strip().lstrip('-+').replace('.', '', 1).isnumeric()


# It isn't necessary to call this function to implement your bikes.py
# functions, but you can use it to create larger lists for testing.
# See the main block below for an example of how to do that.
def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on data to be input.
    """

    # Read and discard header.
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


def total_capacity(stations: List[list]) -> int:
    """Return the total capacity in all stations.

    >>>total_capacity(SAMPLE_STATIONS)
    38
    >>>total_capacity(HANDOUT_STATIONS)
    41
    """
    total_docks = 0
    for station_info in stations:
        total_docks += station_info[CAPACITY]
    return total_docks


def total_bikes_available(stations: List[list]) -> int:
    """Return the total of the bikes available in all stations.

    >>>total_capacity(SAMPLE_STATIONS)
    22
    >>>total_capacity(HANDOUT_STATIONS)
    25
    """
    total_bikes = 0
    for station_info in stations:
        total_bikes += station_info[BIKES_AVAILABLE]
    return total_bikes


def station_wanted(station_id: int, stations: List[list]) -> list:
    """Return wanted station info for the station in stations with id station_id.

    >>>station_wanted(7087, SAMPLE_STATIONS)
    [7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True]
    >>>station_wanted(7088, SAMPLE_STATIONS)
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False]
    """
    wanted_station_info = []
    for station_info in stations:
        if station_id in station_info:
            wanted_station_info = station_info
    return wanted_station_info

####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

SAMPLE_STATIONS = [
    [7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False]]

HANDOUT_STATIONS = [
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 26, 20, 6, True, True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,
     15, 5, 10, True, True]]

#########################################


def clean_data(data: List[list]) -> None:
    """Convert each string in data to an int if and only if it represents a
    whole number, a float if and only if it represents a number that is not a
    whole number, True if and only if it is 'True', False if and only if it is
    'False', and None if and only if it is either 'null' or the empty string.

    >>> d = [['abc', '123', '45.6', 'True', 'False']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, True, False]]
    >>> d = [['ab2'], ['-123'], ['False', '3.2']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], [False, 3.2]]
    """
    for station_info in data:
        for i in range(len(station_info)):
            if is_number(station_info[i]):
                if station_info[i].strip().lstrip('-+').isdigit():
                    station_info[i] = int(station_info[i])
                elif int(station_info[i].split('.')[1]) == 0:
                    station_info[i] = int(station_info[i].split('.')[0])
                else:
                    station_info[i] = float(station_info[i])
            elif station_info[i] == 'True':
                station_info[i] = True
            elif station_info[i] == 'False':
                station_info[i] = False
            elif station_info[i] == '' or station_info[i] == 'null':
                station_info[i] = None

def get_station_info(station_id: int, stations: List[list]) -> list:
    """Return a list containing the following information from stations
    about the station with id number station_id:
        - station name
        - number of bikes available
        - number of docks available
    (in this order)

    Precondition: station_id will appear in stations.

    >>> get_station_info(7087, SAMPLE_STATIONS)
    ['Danforth/Aldridge', 9, 14]
    >>> get_station_info(7088, SAMPLE_STATIONS)
    ['Danforth/Coxwell', 13, 2]
    """
    station_info = []
    for station_list in stations:
        if station_id in station_list:
            station_info.append(station_list[NAME])
            station_info.append(station_list[BIKES_AVAILABLE])
            station_info.append(station_list[DOCKS_AVAILABLE])
    return station_info


def get_total(index: int, stations: List[list]) -> int:
    """Return the sum of the column in stations given by index.

    Precondition: the items in stations at the position
                  that index refers to are ints.

    >>> get_total(BIKES_AVAILABLE, SAMPLE_STATIONS)
    22
    >>> get_total(DOCKS_AVAILABLE, SAMPLE_STATIONS)
    16
    """
    total = 0

    for station_info in stations:
        total += station_info[index]
    return total


def get_station_with_max_bikes(stations: List[list]) -> int:
    """Return the station ID of the station that has the most bikes available.
    If there is a tie for the most available, return the station ID that appears
    first in stations.

    Precondition: len(stations) > 0

    >>> get_station_with_max_bikes(SAMPLE_STATIONS)
    7088
    """
    most_bikes = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(stations)):
        if stations[i][BIKES_AVAILABLE] > most_bikes[BIKES_AVAILABLE]:
            most_bikes = stations[i]
    return most_bikes[ID]


def get_stations_with_n_docks(n: int, stations: List[list]) -> List[int]:
    """Return a list containing the station IDs for the stations in stations
    that have at least n docks available, in the same order as they appear
    in stations.

    Precondition: n >= 0

    >>> get_stations_with_n_docks(2, SAMPLE_STATIONS)
    [7087, 7088]
    >>> get_stations_with_n_docks(5, SAMPLE_STATIONS)
    [7087]
    """
    stations_with_docks = []

    for station_info in stations:
        if station_info[DOCKS_AVAILABLE] >= n:
            stations_with_docks.append(station_info[ID])
    return stations_with_docks


def get_direction(start_id: int, end_id: int, stations: List[list]) -> str:
    """ Return a string that contains the direction to travel to get from
    station start_id to station end_id according to data in stations.

    Precondition: start_id and end_id will appear in stations.

    >>> get_direction(7087, 7088, SAMPLE_STATIONS)
    'SOUTHWEST'
    """
    list_to_compare1 = station_wanted(start_id, stations)
    list_to_compare2 = station_wanted(end_id, stations)

    if list_to_compare1[LATITUDE] > list_to_compare2[LATITUDE]:
        direction = 'SOUTH'
    elif list_to_compare1[LATITUDE] < list_to_compare2[LATITUDE]:
        direction = 'NORTH'
    else:
        direction = ''
    if list_to_compare1[LONGITUDE] < list_to_compare2[LONGITUDE]:
        direction += 'EAST'
    elif list_to_compare1[LONGITUDE] > list_to_compare2[LONGITUDE]:
        direction += 'WEST'
    else:
        direction += ''
    return direction


def rent_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for the station in stations with id station_id as if a single bike was
    removed, leaving an additional dock available. Return True if and only
    if the rental was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available - 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available + 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """

    for station_info in stations:
        if station_id in station_info:
            if station_info[BIKES_AVAILABLE] >= 1 and station_info[IS_RENTING]:
                station_info[BIKES_AVAILABLE] -= 1
                station_info[DOCKS_AVAILABLE] += 1
                return True
    return False


def return_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for station in stations with id station_id as if a single bike was added,
    making an additional dock unavailable. Return True if and only if the
    return was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available + 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available - 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """

    for station_info in stations:
        if station_id in station_info:
            if station_info[DOCKS_AVAILABLE] >= 1 and station_info[IS_RETURNING]:
                station_info[DOCKS_AVAILABLE] -= 1
                station_info[BIKES_AVAILABLE] += 1
                return True
    return False


def balance_all_bikes(stations: List[list]) -> int:
    """Calculate the percentage of bikes available across all stations
    and evenly distribute the bikes so that each station has as close to the
    overall percentage of bikes available as possible. Remove bikes from a
    station if and only if the station is renting and there is a bike
    available to rent, and return a bike if and only if the station is
    allowing returns and there is a dock available. Return the difference
    between the number of bikes rented and the number of bikes returned.

    >>> balance_all_bikes(HANDOUT_STATIONS)
    0
    >>> HANDOUT_STATIONS == [\
     [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17, 14, True, True], \
     [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, \
     15, 8, 7, True, True]]
    True
    """
    goal_percentage_list = []
    count_rented = 0
    count_returned = 0

    percentage = (total_bikes_available(stations) / total_capacity(stations))

    for station_info in stations:
        goal_percentage_list.append(round(station_info[CAPACITY]*percentage))

    for i in range(len(stations)):
        if stations[i][BIKES_AVAILABLE] >= 1 and stations[i][IS_RENTING]:
            while stations[i][BIKES_AVAILABLE] > goal_percentage_list[i]:
                rent_bike(stations[i][ID], stations)
                count_rented += 1
        if stations[i][DOCKS_AVAILABLE] >= 1 and stations[i][IS_RETURNING]:
            while stations[i][BIKES_AVAILABLE] < goal_percentage_list[i]:
                return_bike(stations[i][ID], stations)
                count_returned += 1
    return count_rented - count_returned


if __name__ == '__main__':
    pass

    # #  To test your code with larger lists, you can uncomment the code below to
    # #  read data from the provided CSV file.
    #stations_file = open('stations.csv')
    #bike_stations = csv_to_list(stations_file)
    #clean_data(bike_stations)

    # # For example,
    #print('Testing get_station_with_max_bikes: ', \
    #    balance_all_bikes(bike_stations))