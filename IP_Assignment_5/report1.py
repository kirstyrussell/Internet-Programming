#  Kirsty Russell
#  CS 4720
#  Assignment 4
#  Professor Setzer
#  March 5, 2019

from json_with_dates import loads
import requests

PORT = 21212

# ID Name                    Num Loc     Avg Value    Categories
template = "{:10}  {:20}  {:10}  {:10}  {:20}"
header = template.format("Area ID", "Name","Locations", "Avg Measure", "Categories")
print(header)

r = requests.get("http://localhost:{}/measures/area".format(PORT))
rows = loads(r.text)

for area_rows in rows:
    area_id = area_rows[0]

    # Gets number of locations
    r = requests.get("http://localhost:{}/measures/num_locations/area/{}".format(PORT, area_id))
    num_locations = loads(r.text)

    # Gets Categories
    r = requests.get("http://localhost:{}/measures/categories/area/{}".format(PORT, area_id))
    categories = loads(r.text)
    cat = ""
    for cat_rows in categories:
        cat += " " + str(cat_rows[1])

    # Gets locations
    locations_request = requests.get("http://localhost:{}/measures/locations/area/{}".format(PORT, area_id))
    locations = loads(locations_request.text)
    for location_rows in locations:
        location_id = location_rows[0]

    # Gets avg measurements for location
    measurement_request = requests.get("http://localhost:{}/measures/avg_values/location/{}".format(PORT, area_id))
    measurements = loads(measurement_request.text)
    if measurements is None:
        avg_values = "-----"
    else:
        avg_values = measurements

    # Constructs line from data retrieved earlier
    line = template.format(str(area_id), str(area_rows[1]), str(num_locations), avg_values, str(cat))
    print(line)
