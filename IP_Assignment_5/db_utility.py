#  Kirsty Russell
#  CS 4720
#  Assignment 2
#  Professor Setzer
#  January 31, 2019


import statistics
import db_access


def get_average_measurements_for_area(area_id):
    """
    Returns the average value of all measurements for all locations in the given area.
    Returns None if there are no measurements.
    """
    locations = db_access.get_locations_for_area(area_id)

    if len(locations) == 0:
        return None
    else:
        me_irl = []
        for i in locations:
            for j in db_access.get_measurements_for_location(i[0]):
                me_irl.append(j[1])
        if len(me_irl) == 0:
            return None
        else:
            return str("%.2f" % statistics.mean(me_irl))


def number_of_locations_by_area(area_id):
    """
    Returns the number of locations for the given area.
    """

    if area_id == '':
        raise Exception("area ID could not be ''")

    locations = db_access.get_locations_for_area(area_id)
    return len(locations)
