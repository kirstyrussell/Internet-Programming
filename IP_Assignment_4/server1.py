#  Kirsty Russell
#  CS 4720
#  Assignment 4
#  Professor Setzer
#  March 5, 2019

from bottle import route, run, response
from json_with_dates import dumps
from db_access import get_all_areas, get_categories_for_area, get_locations_for_area
from db_utility import get_average_measurements_for_area, number_of_locations_by_area


# Gets all data from all areas
@route("/measures/area")
def areas():
    data = get_all_areas()
    response.content_type = "application/json"
    return dumps(data)


# Gets the number of locations for an area
@route("/measures/num_locations/area/<area_id:int>")
def num_locations(area_id):
    response.content_type = "application/json"
    data = number_of_locations_by_area(area_id)
    return dumps(data)


# Gets the locations for an area
@route("/measures/locations/area/<area_id:int>")
def locations(area_id):
    response.content_type = "application/json"
    data = get_locations_for_area(area_id)
    return dumps(data)


# Gets the average measurement values for an area
@route("/measures/avg_values/location/<area_id:int>")
def avg_values(area_id):
    response.content_type = "application/json"
    data = get_average_measurements_for_area(area_id)
    return dumps(data)


# Gets the categories for an area
@route("/measures/categories/area/<area_id:int>")
def categories(area_id):
    response.content_type = "application/json"
    data = get_categories_for_area(area_id)
    return dumps(data)


run(host='localhost', port=21212)
